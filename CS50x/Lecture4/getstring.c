#include <stdio.h>

int main(void)
{
    char s[4]; // string needs malloc cus who knows how big a the scanf string is, if let's say s[4] will only save 4 bytes of memory if more than segmentation fault
    //get_string basically loops through each char and checks if another char is coming, if so they will allocate one more byte of memory until no more
    printf("s: ");
    scanf("%s", s); // s is already an address because it's a string which is address of first char
    printf("S; %s\n", s);
}
