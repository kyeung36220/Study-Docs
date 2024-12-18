#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <string.h>

int points[26] = {1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 1, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10};

int point_sum(string x);

int main(void)
{
    string p1 = get_string("Player 1: ");
    string p2 = get_string("Player 2: ");
    if (point_sum(p1) > point_sum(p2))
    {
        printf("Player 1 Wins!\n");
    }
    else if (point_sum(p1) < point_sum(p2))
    {
        printf("Player 2 Wins!\n");
    }
    else
    {
        printf("Tie!\n");
    }
    // printf("P1: %d\nP2: %d\n", point_sum(p1), point_sum(p2));
}

int point_sum(string x)
{
    int sum = 0;
    for (int i = 0, length = strlen(x); i < length; i++)
    {
        if (isupper(x[i]))
        {
            sum += points[x[i] - 'A'];
        }
        else if (islower(x[i]))
        {
            sum += points[x[i] - 'a'];
        }
    }
    return sum;
}
