#include <stdio.h>
#include <stdint.h>
#include <stdlib.h>

//Walkthrough by Max 10/6

typedef unsigned char BYTE;

int main(int argc, char *argv[])
{
    if (argc != 2)
    {
        printf("Correct usage is: ./recover *file*\n");
        return 1;
    }

    char currChar = 'c';
    unsigned char buffer[512];
    int imageCount = 0;
    char imageName [8];
    FILE *file = fopen(argv[1], "r");
    FILE *outFile = NULL;

    //if NULL, can't open

    while(fread(buffer, 1, 512, file) == 512 && feof(file) == 0)
    {
        if (buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff && (buffer[3] & 0xf0) == 0xe0)
        {
            sprintf(imageName, "%03i.jpg", imageCount);
            outFile = fopen(imageName, "w");
            fwrite(buffer, 1, 512, outFile);
            imageCount++;
        }
        else
        {
            if (imageCount > 0)
            {
                fwrite(buffer, 1, 512, outFile);
            }
        }
    }

    fclose(file);
}
