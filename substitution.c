#include <cs50.h>
#include <stdio.h>
#include <string.h>

//Graham Stodolski CS50

int main(int argc, string argv[])
{
    if (argc != 2)  //ensures word count is two
    {
        printf("Usage: ./substitution key\n");
        return 1;
    }

    if (strlen(argv[1]) != 26)  //ensures key is 26 characters long
    {
        printf("Key must be 26 characters long.\n");
        return 1;
    }

    for (int i = 0;  i < strlen(argv[1]); i++)  //deals with invalid characters
    {
        if (!('A' <= argv[1][i] && argv[1][i] <= 'Z') && !('a' <= argv[1][i] && argv[1][i] <= 'z'))
        {
            printf("Key must only contain alphabetic characters.\n");
            return 1;
        }
    }

    int duplicates = 0;
    for (int k = 0;  k < strlen(argv[1]); k++) //cycles through each character and compares it to every other character
    {
        duplicates = 0;
        for (int l = 0;  l < strlen(argv[1]); l++)
        {
            if (argv[1][k] == argv[1][l])
            {
                duplicates++;
                if (duplicates == 2)  //if there are 2 duplicates (there will always be 1 since argv[1][k] == argv[1][k]), program ends
                {
                    printf("Key must not contain repeated characters.\n");
                    return 1;
                }
            }
        }
    }

    string plainText = get_string("plaintext:  ");  //prompts human for plain text to be encrypted
    int index = 0;

    printf("ciphertext: ");
    for (int j = 0; j < strlen(plainText); j++)  //cycles through each character of plain text
    {
        if ('a' <= plainText[j] && plainText[j] <= 'z')  //checks if plain text char is lowercase
        {
            index = plainText[j] - 'a';  //calculates index for argv
            if ('A' <= argv[1][index] && argv[1][index] <= 'Z')  //ensures case of plain text is retained
            {
                printf("%c", argv[1][index] + 32);
            }
            else
            {
                printf("%c", argv[1][index]);
            }
        }
        else if ('A' <= plainText[j] && plainText[j] <= 'Z')  //checks if plain text char is uppercase
        {
            index = plainText[j] - 'A';  //calculates index for argv
            if ('a' <= argv[1][index] && argv[1][index] <= 'z')  //ensures case of plain text is retained
            {
                printf("%c", argv[1][index] - 32);
            }
            else
            {
                printf("%c", argv[1][index]);
            }
        }
        else
        {
            printf("%c", plainText[j]);  //prints anything that's not a letter
        }
    }
    printf("\n");
}