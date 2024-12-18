import sys
import math


def main():
    while True:
        number = input("Number: ")
        if number.isdigit() == True:
            number = int(number)
            break
        else:
            sys.exit("INVALID")

    if valid_card(number) == False:
        print("INVALID")

    elif amex_checker(number) == True:
        print("AMEX")
    elif master_checker(number) == True:
        print("MASTERCARD")
    elif visa_checker(number) == True:
        print("VISA")

    else:
        print("INVALID")


def valid_card(number):
    current_number = int(number)
    last_digit = current_number % 10
    digit_number = 1
    number_sum = 0
    while current_number > 0:
        if digit_number % 2 != 0:
            number_sum += last_digit
        elif digit_number % 2 == 0 and last_digit * 2 < 10:
            number_sum += last_digit * 2
        elif digit_number % 2 == 0 and last_digit * 2 >= 10:
            last_digit *= 2
            number_sum += last_digit % 10 + 1

        digit_number += 1
        current_number = current_number // 10
        last_digit = current_number % 10

    if number_sum % 10 == 0:
        return True
    else:
        return False


def amex_checker(number):
    amex_length = 15
    if math.floor(number / pow(10, amex_length - 2)) == 34 or math.floor(number / pow(10, amex_length - 2)) == 37:
        return True


def master_checker(number):
    mc_length = 16
    if math.floor(number / pow(10, mc_length - 2)) >= 51 and math.floor(number / pow(10, mc_length - 2)) <= 55:
        return True


def visa_checker(number):
    visa_length_small = 13
    visa_length_big = 16
    if math.floor(number / pow(10, visa_length_small - 1)) == 4 or math.floor(number / pow(10, visa_length_big - 1)) == 4:
        return True


if __name__ == "__main__":
    main()
