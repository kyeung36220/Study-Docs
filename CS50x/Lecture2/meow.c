#include <cs50.h>
#include <stdio.h>

void meow(int n);

int main(void)
{
    meow(30);
}

void meow(int n)
{
    for (int i = 0; i < n; i += 1)
    {
        printf("meow\n");
    }

}
