#include <cs50.h>
#include <ctype.h>
#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

bool digit_check(char x[]);

int main(int argc, string argv[])
{
    if (argc != 2) // check if user typed more than 1 thing
    {
        printf("Usage: ./caesar key\n");
        return 1;
    }

    else // check if user put in digit or not(if not then it'll just deny it)
    {
        bool is_number = digit_check(argv[1]);
        if (is_number == false)
        {
            printf("Usage: ./caesar key\n");
            return 1;
        }
    }

    int key = atoi(argv[1]); // convert string to integer

    string plaintext = get_string("plaintext: "); // get user's text
    printf("ciphertext: ");

    for (int i = 0; i < strlen(plaintext); i++)
    {
        if (isalpha(plaintext[i]))
        {
            if isupper (plaintext[i])
            {
                printf("%c", (plaintext[i] - 'A' + key) % 26 + 'A');
            }

            else
            {
                printf("%c", (plaintext[i] - 'a' + key) % 26 + 'a');
            }
        }
        else
        {
            printf("%c", plaintext[i]);
        }
    }
    printf("\n");

    return 0;
}

bool digit_check(char x[])
{
    bool is_number = false;
    for (int i = 0; i < strlen(x); i++)
    {
        if (isdigit(x[i]))
        {
            is_number = true;
        }
        else
        {
            is_number = false;
            break;
        }
    }
    return is_number;
}
