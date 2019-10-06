#include <stdio.h>
#include <stdlib.h>

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
    char *imageName = "strang";
    FILE *file = fopen(argv[1], "r");

    while ((currChar = fgetc(file)) != EOF)  //iterate thru chars
    {
        fread(buffer, 1, 512, file);
        if (buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff && (buffer[3] & 0xf0) == 0xe0)
        {
            imageCount++;
            sprintf(imageName, "%03i.jpg", imageCount);
            FILE *img = fopen(imageName, "w");
        }
    }
}
