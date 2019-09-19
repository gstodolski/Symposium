#include <cs50.h>
#include <stdio.h>
#include <string.h>

//Graham Stodolski CS50

int main(int argc, string argv[]) {

    if (argc != 2) {
        printf("Usage: ./substitution key\n");
        return 1;
    }

    if (strlen(argv[1]) != 26) {
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
    for (int k = 0;  k < strlen(argv[1]); k++)
    {
        duplicates = 0;
        for (int l = 0;  l < strlen(argv[1]); l++)
        {
            if (argv[1][k] == argv[1][l])
            {
                duplicates++;
                if (duplicates == 2)
                {
                    printf("Key must not contain repeated characters.\n");
                    return 1;
                }
            }
        }
    }

    string plainText = get_string("plaintext:  ");
    int index = 0;

    printf("ciphertext: ");
    for (int j = 0; j < strlen(plainText); j++) {
        if ('a' <= plainText[j] && plainText[j] <= 'z') {
            index = plainText[j] - 'a';
            if ('A' <= argv[1][index] && argv[1][index] <= 'Z' ) {
                printf("%c", argv[1][index] + 32);
            }
            else {
                printf("%c", argv[1][index]);
            }
        }
        else if ('A' <= plainText[j] && plainText[j] <= 'Z') {
            index = plainText[j] - 'A';
            if ('a' <= argv[1][index] && argv[1][index] <= 'z' ) {
                printf("%c", argv[1][index] - 32);
            }
            else {
                printf("%c", argv[1][index]);
            }
        }
        else {
            printf("%c", plainText[j]);
        }
    }
    printf("\n");
}