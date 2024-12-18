def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    #must start with at least 2 letters
    if s[0:2].isalpha() == False:
        return False

    #max of 6 characters and minimum of 2 characters
    elif len(s) < 2 or len(s) > 6:
        return False

    #numbers not in the middle and first number not a 0
    number_counter = 0
    for c in s:
        # if number has already presented itself and a letter arises then False
        if c.isalpha() == True and number_counter > 0:
            return False
        # if first number is 0 then false
        elif c.isdigit() == True and number_counter == 0 and int(c) == 0:
            return False
        #adding to number counter to be over 0
        if c.isdigit() == True:
            number_counter += 1


    #no periods spaces or punctuation
    for c in s:
        if c.isalnum() == False:
            return False

    #if all is good then true
    else:
        return True


main()

if __name__ == "__main__":
    main()
