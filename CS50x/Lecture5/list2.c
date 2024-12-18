#include <stdio.h>
#include <stdlib.h>

typedef struct node
{
    int number;
    struct node *next;
} node;

int main(int argc, char *argv[])
{
    node *list = NULL;

    for (int i = 1; i < argc; i++)
    {
        int number = atoi(argv[i]);

        node *n = malloc(sizeof(node));
        if (n == NULL)
        {
            //free memory thus far
            return 1;
        }
        n->number = number; // same as (*n).number = number
        //n-> next = NULL;

        n->next = list; // set node to where list is at, which prevents orphaned varibles for example if you are at 2 if list = n then 1 would be orphaned
        list = n;
    }
    //print entire list
    node *pointer = list; // ptr is better but i will use pointer here
    while (pointer != NULL)
    {
        printf("%i\n", pointer->number);
        pointer = pointer->next;
    }
}
