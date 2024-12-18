# Password Manager
#### Video Demo:  https://youtu.be/afLy2dJpxNA

## Description:
Password Manager is a python application in where a user can input and store passwords from various websites and retrieve the passwords at any time.

### Login:
In this program, there is a login page where the user will need to put in a password. If the user is new, then they will be prompted to make a password. This prevents unwanted people to be able to access the passwords from the user. If the user types the wrong password, the user will be kicked out of the program. Once the user successfully logs in, they will see the Main Menu.

### Main Menu:
There are 4 main actions that can be done in this application which is shown in the Main Menu:
- Input Password
- Retrieve Password
- Edit Password
- Delete Account (deleting csv file)

### Input Password:
In input password, the user will be prompted to give the website that they want to save a password for. If the website is not in the csv file, there will be a prompt asking for the password. Once the user enters a password, the program will append the information (website and password) to the csv file. If the website is already in the csv file, there will be a prompt that asks whether the user wants to replace the existing password for that website. If the user wants to replace, there will be a prompt asking for the new password and once entered, the program will use the Pandas library to replace the website's password.

### Retrieve Password:
In retrieve password, the user will be prompted for the website they want to receive a password for. If the website is in the csv file, the program will use the Tabulate Library to show a table with the website and password. If the website is not in the csv file, the user will see a print saying "Website not found."

### Edit Password:
In edit password, the user will see a menu with 3 options:
- Change login password
- Change website password
- Exit

If the user wants to change their login password, they will be prompted for the password and the Pandas library will replace the existing UserLogin password with the new password

If the user wants to change an existing website password, the user will be prompted to type in the website. If the website is found, then the user can type the password and the program will use the Pandas Library to change the existing website password in the csv file. If the website is not found, the user will see "Website not found"

If the user chooses to exit, they will go back to the main menu

### Delete Account:
This will delete the entire csv file, effectively destroying all the passwords stored.


### Encryption:
Additionally, the program also encrypts all the passwords before slotting them in the csv file. When looking at the raw csv file with the website and passwords, they will see something like, (youtube.com, +-/-), where the password is encrypted. The program will decrypt the password once a user wants to retrieve a password.

## Requirements:
This programs requires the user to install colorama, tabulate, and pandas. Colorama is simply a UI enhancement which brings colors into strings. I used this to show red when the user did something wrong or show green when the user successfully did something. Tabulate is only used in the retrieve function and the sole purpose is to format the string when the user wants to see the password. Pandas is essential for this program as it is the reason why this program can edit certain values in the csv file without deleting the entire file.
