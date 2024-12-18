#include <stdio.h>

void swap(int *a, int *b); //

int main (void)
{
    int x = 1;
    int y = 2;

    printf("x is %i, y is %i\n", x, y);
    swap(&x,&y);
    printf("SWAPPED: x is %i, y is %i\n", x, y);

}

void swap(int *a, int *b) // remember to put star to pass in addresses
{
    //int tmp = a; passing by value not reference
    //a = b;
    //b = tmp;

    int tmp = *a; // passing by reference
    *a = *b;
    *b = tmp;
}

//buffer overflow just means stack/heap overflow which means using more memory that there is
