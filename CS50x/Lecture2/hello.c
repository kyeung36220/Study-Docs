#include <stdio.h> //prototype of get_string and has code included
#include <cs50.h>

int main(void)
{
    string name = get_string("What's your name? ");
    printf("hello, %s\n", name);
}


//preprocessing is to get all hashtag includes into exquivalents like stdio.h lib only uses get_string
//compiling makes C into assembly
//assembling takes assembly code to binary
// combines all binary of your code and libraries and combiens them all into one
