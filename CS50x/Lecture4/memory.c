#include <stdio.h>
#include <stdlib.h>

int main(void)
{
    int *x = malloc(3 * sizeof(int)); // gets size of memory of and integer
    // if want 3 integers and can make array to multiply by 3, same is i[3]

    x[0] = 72;
    x[1] = 73;
    x[2] = 33;
    free(x)
}

//valgrind ./memory shows issues with memory like if index is wrong or if you didn't free a malloc
//if valgrind no worries then will say no leaks
