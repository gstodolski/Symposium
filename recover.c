#include <stdio.h>
#include <stdint.h>
#include <stdlib.h>

//Help from Max and Drew W. 10/6

int main(int argc, char *argv[])
{
    if (argc != 2)  //ensures input is correct
    {
        printf("Correct usage is: ./recover *file*\n");
        return 1;
    }

    unsigned char buffer[512];
    int imageCount = 0;
    char imageName [8];
    FILE *file = fopen(argv[1], "r");
    FILE *outFile = NULL;

    while (fread(buffer, 1, 512, file) == 512 && feof(file) == 0)  //reading through file and checking if its not done
    {
        if (buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff && (buffer[3] & 0xf0) == 0xe0)  //checks for jpg
        {
            sprintf(imageName, "%03i.jpg", imageCount);  //correctly names each image
            outFile = fopen(imageName, "w");
            fwrite(buffer, 1, 512, outFile);
            imageCount++;  //counter for images
        }
        else
        {
            if (imageCount > 0)
            {
                fwrite(buffer, 1, 512, outFile);
            }
        }
    }

    fclose(file);  //closes card.raw
}
