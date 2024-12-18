#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <cs50.h>

int main(int argc, char *argv[])
{
    // Accept a single command-line argument
    if (argc != 2)
    {
        printf("Usage: ./recover FILE\n");
        return 1;
    }

    // Open the memory card
    FILE *card = fopen(argv[1], "r");
    if (card == NULL)
    {
        printf("Could not open %s.\n", argv[1]);
        return 2;
    }

    // file name declaration
    char filename[8];

    // output file
    FILE *output;

    // Create a buffer for a block of data
    uint8_t buffer[512];

    // keep track of jpg number
    int img_num = 0;

    // While there's still data left to read from the memory card
    while (fread(buffer, 1, 512, card) == 512)
    {
        if (buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff &&
            (buffer[3] & 0xf0) == 0xe0)
        {
            if (img_num == 0)
            {
                sprintf(filename, "%03i.jpg", img_num);
                output = fopen(filename, "w");
                fwrite(buffer, 1, 512, output);
                img_num += 1;
            }

            else if (img_num > 0)
            {
                fclose(output);
                sprintf(filename, "%03i.jpg", img_num);
                output = fopen(filename, "w");
                fwrite(buffer, 1, 512, output);
                img_num += 1;
            }
        }

        else if (img_num > 0)
        {
            fwrite(buffer, 1, 512, output);
        }
    }
    fclose(card);
    fclose(output);
}
