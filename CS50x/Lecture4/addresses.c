#include <stdio.h>

int main(void)
{
    int n = 50; // n is just the start of the address of array of characters
    int *p = &n; //star lets you declare/store address and & tells computer that this variable is an address
    printf("%i\n", *p); //star here means GO THERE (weirdly different meaning from above star)
    // can also do %p to get pointer of variable
}

// STAR* is GO TO and AMPRASAND& is FIGURES OUT WHAT THIS ADDRESS IS
