#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int height;
    do
    {
        height = get_int("Height: "); //prompts human for desired height
    }
    while (0 >= height || height >= 9); //ensures input is between 1 and 8
    
    for (int row = 0; row < height; row++)
    {
        for (int i = 0; i < (height - row - 1); i++)
        {
            printf(" ");
        }
        for (int j = 0; j < row + 1; j++)
        {
            printf("#");
        }
        printf("  ");
        for (int k = 0; k < row + 1; k++)
        {
            printf("#");
        }
        printf("\n");
    }
}
