#include <stdio.h>

int main(void)
{
    int n; // no need to malloc cus integer will always be 4 bytes
    printf("n: ");
    scanf("%i", &n); // this is basically getting input from user, need to pass in address so that scanf can change value in the memory
    printf("n: %i\n", n);
}
