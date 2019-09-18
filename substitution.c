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

    string plainText = get_string("plaintext:  ");
    int index = 0;

    printf("ciphertext: ");
    for (int i = 0; i < strlen(plainText); i++) {
        if ('a' <= plainText[i] && plainText[i] <= 'z') {
            index = plainText[i] - 'a';
            if ('A' <= argv[1][index] && argv[1][index] <= 'Z' ) {
                printf("%c", argv[1][index] + 32);
            }
            else {
                printf("%c", argv[1][index]);
            }
        }
        else if ('A' <= plainText[i] && plainText[i] <= 'Z') {
            index = plainText[i] - 'A';
            if ('a' <= argv[1][index] && argv[1][index] <= 'z' ) {
                printf("%c", argv[1][index] - 32);
            }
            else {
                printf("%c", argv[1][index]);
            }
        }
        else {
            printf("%c", plainText[i]);
        }
    }
    printf("\n");
}