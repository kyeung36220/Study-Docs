#include <cs50.h>
#include <math.h>
#include <stdio.h>

int main(void)
{
    long number = get_long("Number: "); // inputted number
    long checksum = number;
    int mult_numbers = 0;
    int norm_numbers = 0;
    int digit_number = 0;
    int validity_sum = 0;
    bool validity_check = true;

    int amex_length = 15;
    int mc_length = 16;
    int visa_length_small = 13;
    int visa_length_big = 16;

    while (checksum > 0) // check sum
    {
        digit_number += 1;

        long last_digit = checksum % 10;

        if (digit_number % 2 == 0 && last_digit * 2 < 10) // if even then add and multiply
        {
            mult_numbers += last_digit * 2;
        }

        else if (digit_number % 2 == 0 && last_digit * 2 >= 10)
        {
            last_digit *= 2;
            mult_numbers += last_digit % 10 + 1;
        }

        else // if odd then add
        {
            norm_numbers += last_digit;
        }
        checksum /= 10;
    }
    validity_sum = mult_numbers + norm_numbers;

    if (validity_sum % 10 != 0)
    {
        validity_check = false;
        printf("INVALID\n");
    }
    else
    {
        validity_check = true;
    }

    if (validity_check == true)
    {
        if (floor(number / pow(10, amex_length - 2)) == 34 ||
            floor(number / pow(10, amex_length - 2)) == 37) // amex
        {
            printf("AMEX\n");
        }
        else if (floor(number / pow(10, mc_length - 2)) >= 51 &&
                 floor(number / pow(10, mc_length - 2)) <= 55)
        {
            printf("MASTERCARD\n");
        }
        else if (floor(number / pow(10, visa_length_small - 1)) == 4 ||
                 floor(number / pow(10, visa_length_big - 1)) == 4)
        {
            printf("VISA\n");
        }
        else
        {
            printf("INVALID\n");
        }
    }
}
