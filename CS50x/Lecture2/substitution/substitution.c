#include <cs50.h>
#include <ctype.h>
#include <math.h>
#include <stdio.h>
#include <string.h>

bool alph_check(y, x);

int main(int argc, char *argv[])
{
    bool all_letters = alph_check(argc, argv);
}

bool alph_check(int argc, char *argv[])
{
    bool all_alph = true;
    for (int i = 0; i < argc; i++)
    {
        if (isalpha(argv[i][0]))
        {
            all_alph = true;
        }
        else
        {
            all_alph = false;
            break;
        }
    }
    return all_alph;
}
