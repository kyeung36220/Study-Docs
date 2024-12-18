name = input("What's your name? ")
#plan to write for w allows user to change contents when writing w, w will clear file everytime before writing
#a will instead append or add to the file instead of wiping
#with statement will auto open and close file

with open("names.txt", "a") as file:
    file.write(name + "\n")

