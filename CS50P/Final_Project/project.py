import sys
import csv
import pandas as pd
from colorama import Fore, init
from tabulate import tabulate
import os

init(autoreset=True) #To reset color after color change of text (colorama)

def main():

    clear_screen()

    try:
        existing_login()
    except FileNotFoundError:
        new_login()

    #Main menu
    while True:
        print("[1] Enter new password")
        print("[2] Retrieve password")
        print("[3] Edit password")
        print("[4] Delete account")
        print("[5] Exit\n")
        choice = input("Enter your choice: ").strip()

        clear_screen()

        if choice == '1':
            insert()
        elif choice == '2':
            retrieve()
        elif choice == '3':
            edit()
        elif choice == '4':
            delete()
        elif choice == '5':
            sys.exit(Fore.GREEN + "Thank you and have a good day!\n")
        else:
            print("Please enter a number 1 through 5.\n")


def insert():
    website = input("Enter the link: ").lower()

    #checks if website is already in csv file
    found = False
    with open('passwords.csv', 'r') as file:
        reader = csv.reader(file)
        line = -2
        for row in reader:
            line += 1
            if row[0] == website:
                found = True
                break

    #if link in csv file, asks if want to replace
    while True:
        if found:
            print("It seems there is already a password logged for this website.")
            edit = input("Do you want to edit the existing password? (Y/N) ").strip()

            #if want to replace then uses find_and_replace function to replace
            if edit.lower() == "yes" or edit.lower() == "y":
                password = input("Enter your new password: ")
                encrypted_password = encrypt(password)
                find_and_replace(line, encrypted_password)
                clear_screen()
                print(Fore.GREEN + "Password updated successfully!\n")
                return

            #if don't want to replace then
            elif edit.lower() == "no" or edit.lower() == "n":
                clear_screen()
                return

            #if enters invalid prompt then loops back
            else:
                print("Please enter Yes or No")

        #if not found then does not loop
        else:
            break

    #if not found then appends new line with new website and password
    with open('passwords.csv', 'a', newline='') as file:
        password = input("Enter your password: ")
        writer = csv.writer(file)
        encrypted_password = encrypt(password)
        writer.writerow([website, encrypted_password])

    #when done, clears screen then goes back to main menu
    clear_screen()
    print(Fore.GREEN + "Password added successfully!\n")


def retrieve():
    website = input("Enter the website: ").lower()

    #opens csv file in reader mode
    with open('passwords.csv', 'r') as file:
        reader = csv.reader(file)

        #checks if website is in csv file and if so then edits value using pandas lib
        for row in reader:
            if row[0] == website:
                decrypted_password = decrypt(row[1])
                clear_screen()
                print(tabulate([[website, decrypted_password]], ["link", "password"], tablefmt="outline"), "\n")
                return

    #if not found then clears screen and returns back to main menu
    clear_screen()
    print(Fore.RED + "Website not found.")

def edit():

    #edit menu where user can choose to edit login password or a link password
    while True:
        print("[1] Edit login password")
        print("[2] Edit link password")
        print("[3] Exit\n")
        choice = input("Enter your choice: ").strip()
        clear_screen()

        #if user enters valid prompt then moves on
        if choice == '1' or choice == '2' or choice == '3':
            break

        #if user enters invalid prompt then loops back to menu
        else:
            print("Please enter 1, 2, or 3\n")

    #if user wants to edit login password
    if choice == '1':
        while True:
            password = input("Create your new password: ")
            reverification = input("Type your new password again: ")

            #if password and reverification are the same then updates csv file
            if password == reverification:
                encrypted_password = encrypt(password)
                find_and_replace(0, encrypted_password)
                clear_screen()
                print(Fore.GREEN + "Password updated successfully!\n")
                return

            #if password and reverification are not the same then loops back to beginning of choice 1
            else:
                clear_screen()
                print(Fore.RED + "Your passwords did not match. Try again.\n")

    #if user wants to change link password
    elif choice == '2':
        while True:
            website = input("Enter link: ").lower()

            #checks to see if link is in csv file
            found = False
            with open('passwords.csv', 'r') as file:
                reader = csv.reader(file)
                line = -2
                for row in reader:
                    line += 1
                    if row[0] == website:
                        found = True
                        break

            #if link exists in csv file then prompts user for new password and replaces
            if found:
                    password = input("Enter your new password: ")
                    encrypted_password = encrypt(password)
                    find_and_replace(line, encrypted_password)
                    clear_screen()
                    print(Fore.GREEN + "Password updated successfully!\n")
                    return

            #if link doesn't exists in csv file then returns back to main menu
            else:
                clear_screen()
                print(Fore.RED + "Link not found.\n")
                return

    #if user wants to exit then goes back to main menu
    elif choice == '3':
        clear_screen()
        return

#if user wants to delete account then deletes csv file and sys.exit
def delete():
    os.remove("passwords.csv")
    print(Fore.GREEN + "Account deleted\n")
    sys.exit("Thank you for using Password Manager.\n")

#if passwords.csv file doesn't exist then considered new user
def new_login():
    print("Let's create a new account.\n")

    #prompts user for password
    while True:
        password = input("Create your password: ")
        reverification = input("Type your password again: ")
        if password == reverification:
            clear_screen()
            print(Fore.GREEN + "Success! You account has been made.\n")
            break
        else:
            clear_screen()
            print(Fore.RED + "Your passwords did not match. Try again.\n")

    #creates file and writes header
    with open('passwords.csv', "w", newline = '') as new_file:
        writer = csv.writer(new_file)
        writer.writerow(["website","password"])

    #writes login password
    with open('passwords.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        encrypted_password = encrypt(password)
        writer.writerow(["UserLogin", encrypted_password])

#if passwords.csv file does exist then is existing user
def existing_login():
    print("Welcome to Password Manager!\n")
    line_count = 0

    #prompts user for password
    with open('passwords.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == "UserLogin":
                password = input("Please enter your password: ")

                #if user enters password that matches csv file UserLogin then successful
                if password == decrypt(row[1]):
                    clear_screen()
                    print(Fore.GREEN + "Login successful!\n")
                    return
            line_count += 1

        #if csv file exists and user types incorrect password then sys.exit user
        if line_count > 1:
            clear_screen()
            sys.exit(Fore.RED + "Incorrect password. Kicking user out.\n")

        #if csv file not found then raises error which goes to new_login function
        if line_count <= 1:
            raise FileNotFoundError

def encrypt(s, shift=6):
    encrypted_password = ""

    #moves ascii of each char in s by adding shift amount
    for char in s:
        encrypted_char = chr((ord(char) + shift))
        encrypted_password += encrypted_char
    return encrypted_password

def decrypt(s, shift=6):
    decrypted_password = ""

    #moves ascii of each char in s by subtracting shift amount
    for char in s:
        decrypted_char = chr((ord(char) - shift))
        decrypted_password += decrypted_char
    return decrypted_password

#clears screen
def clear_screen():
    os.system('clear')

#finds line and uses pandas to replace value of specific value using index number
def find_and_replace(line, encrypted_password):
    df = pd.read_csv("passwords.csv")
    df.loc[line,'password'] = encrypted_password
    df.to_csv("passwords.csv", index=False)


if __name__ == "__main__":
    main()
