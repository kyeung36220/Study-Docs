#include <cs50.h>
#include <stdio.h>

bool valid_triangle(int x, int y, int z);

int main(void)
{
    int side_x = get_int("First side length: ");
    int side_y = get_int("Second side length: ");
    int side_z = get_int("Third side length: ");
    bool validity_of_triangle = valid_triangle(side_x, side_y, side_z);
    if (validity_of_triangle == true)
    {
        printf("Is a triangle\n");
    }
    else
    {
        printf("Is not a triangle\n");
    }
}

bool valid_triangle(int x, int y, int z)
{
    bool validity = true;
    if (x < 0 && y < 0 && z < 0) //check if positive
    {
        validity = false;
    }
    if ((x + y) < z || (x + z) < y || (y + z) < x)
    {
        validity = false;
    }
    return validity;
}
