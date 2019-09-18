#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <math.h>

//Graham Stodolski CS50

int main(void) {

    string text = get_string("Text: ");

    int letters = 0;
    int words = 1;
    int sentences = 0;

    for (int i = 0; i < strlen(text); i++) {  //cycles through characters in text
        if (('A' <= text[i] && text[i] <= 'Z') || ('a' <= text[i] && text[i] <= 'z')) {  //checks if current character is a letter
            letters++;
        }
        else if (text[i] == ' ') {  //checks for spaces
            words++;
        }
        else if (text[i] == '.' || text[i] == '!' || text[i] == '?') {  //checks for punctuation
            sentences++;
        }
    }

    float index = 0.0588 * (letters * 100)/(words) - 0.296 * (sentences * 100)/(words) - 15.8;  //Coleman-Liau index
    index = round(index);
    if (index < 1) {
        printf("Before Grade 1\n");
    }
    else if (index >= 16) {
        printf("Grade 16+\n");
    }
    else {
        printf("Grade %.0f\n", index);
    }
}