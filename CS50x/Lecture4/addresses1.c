#include <stdio.h>
#include <cs50.h>

int main(void)
{
    char *s = "Hi!"; // string is char *s, char* is just the address of a star which tells the system that it needs to print all chars until \0
    // quotes already will replace & but if a variable needs & like example "&n"
    // typedef char*string has been making string into char*
    printf("%p\n", s);
    printf("%p\n", &s[0]);
    printf("%p\n", &s[1]);
}
