#include <stdbool.h>
#include <stdio.h>

typedef unsigned char BYTE;

int main(int argc, char *argv[])
{
    if (argc != 2)
    {
        printf("Usage: ./count INPUT\n");  // ends program if input is incorrect
        return 1;
    }

    FILE *file = fopen(argv[1], "r");
    if (!file)
    {
        printf("Could not open file.\n");  // ends program if can't open file
        return 1;
    }

    int count = 0;
    while (true)
    {
        BYTE b;
        fread(&b, 1, 1, file);

        if (feof(file))
        {
            break;  // ends while loop if fread has reached EOF
        }

        if (b >= 0 && b <= 127)  // checks if byte indicates the first byte in a one-byte sequence
        {
            count++;
        }
        if (b >= 194 && b <= 255)  // checks if byte indicates the first byte in a longer sequence
        {
            count++;
        }
    }
    printf("Number of characters: %i\n", count);  // outputs number of characters
}