#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int table[100];
    for (int i = 1; i <= 100; i++)
    {
        table[i] = i;
        printf("%d ", table[i]);
    }
    printf("\n");
}
