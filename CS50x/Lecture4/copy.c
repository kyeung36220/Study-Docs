#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(void)
{
    char *s = get_string("s: ");

    if (s== NULL)// check if there is enough memory
    {
        return 1;
    }

    char *t = malloc(strlen(s) + 1);// adding 1 for null \0

    if (t== NULL)// check if there is enough memory
    {
        return 1;
    }

    for (int i = 0, n = strlen(s); i < n + 1; i++)// adding 1 for null character
    {
        t[i] = s[i]; // copying each char over can also use strcpy(s, t)
    }
    if (strlen(t) > 0)
    {
        t[0] = toupper(t[0]);
    }


    //string t = s; copying address right now, NOT VALUE

    printf("s is %s\n", s);
    printf("t is %s\n", t);

    free(t) // free memory that I malloc'ed and give it back
    return 0
}
