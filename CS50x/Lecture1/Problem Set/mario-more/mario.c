#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int height;
    int level = 0;

    do
    {
        height = get_int("Height: ");
    }
    while (height <= 0 || height > 8);

    for (int i = height; i > 0; i -= 1)
    {
        for (int j = height - level - 1; j > 0; j -= 1)
        {
            printf(" ");
        }

        for (int k = 0; k < level + 1; k += 1)
        {
            printf("#");
        }

        printf("  ");

        for (int m = 0; m < level + 1; m += 1)
        {
            printf("#");
        }

        printf("\n");
        level += 1;
    }
}
