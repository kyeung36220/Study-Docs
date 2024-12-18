#include <stdio.h>
#include <stdlib.h>

int main(void)
{
    int *list = malloc(3 * sizeof(int)); // give me memory at the address of list of 3 * whatever the size of an integer is
    if (list == NULL)
    {
        return 1;
    }

    list[0] = 1;
    list[1] = 2;
    list[2] = 3;

    int *tmp = malloc(4 * sizeof(int));
    if (tmp == NULL)
    {
        free(list); // will free list as well because we aleardy malloc list before this
        return 1;
    }

    for (int i = 0; i < 3; i++)
    {
        tmp[i] = list[i]; // copy tmp to list
    }
    tmp[3] = 4; // add that last digit

    free(list);
    list = tmp; // updating address of list to point to tmp

    for (int i = 0; i < 4; i++)
    {
        printf("%i\n", list[i]);
    }

    free(list);
    return 0;
}
