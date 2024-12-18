#include <stdio.h>
#include <stdint.h>

typedef uint8_t BYTE; // give me 1 byte that is unassigned

int main(int argc, char*argv[]) // remember char* is string
// can run ./cp cat.jpg backup.jpg and will copy from cat to backup
{
    FILE *src = fopen(argv[1], "rb"); // open source file in read mode but binary so readbinary = rb
    FILE *dst = fopen(argv[2], "wb"); // destination file in write mode in binary so writebinary = wb

    BYTE b;

    while (fread(&b, sizeof(b), 1, src) != 0)// while there are bytes to read in file, read 1 byte at a time from source and !=0 means if not failed
    {
        fwrite(&b, sizeof(b), 1, dst); // go to address of b and write it one byte at a time to destination file
    }

    fclose(dst);
    fclose(src);
}
