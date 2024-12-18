#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int s = get_string("i: "); // different addresses means can't be compared cus is comparing addresses, NOT strings
    //like what if t changes, why would s also change, so 2 different places in memory
    int t = get_string("j: ");

    printf("%p\n", s);
    printf("%p\n", t);
}
