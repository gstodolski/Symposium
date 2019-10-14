// Implements a dictionary's functionality

#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <strings.h>
#include <ctype.h>
#include "dictionary.h"

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
}
node;

// Number of buckets in hash table
const unsigned int N = 1000;

// Hash table
node *table[N];

int wordCount = 0;
int indexValue;

// Returns true if word is in dictionary else false
bool check(const char *word)
{
    indexValue = hash(word);
    node *cursor = table[indexValue];
    while (cursor != NULL)
    {
        if ((strcasecmp(cursor->word, word)) == 0)
        {
            return true;
        }
        else
        {
            cursor = cursor->next;
        }
    }

    return false;
}

// Hashes word to a number
unsigned int hash(const char *word)  // djb2 hash function: https://stackoverflow.com/questions/7666509/hash-function-for-string
{
    unsigned int hash = 5381;
    int c;

    while ((c = *word++))
    {
        hash = ((hash << 5) + hash) + tolower(c);
    }

    return hash % 1000;
}

// Loads dictionary into memory, returning true if successful else false
bool load(const char *dictionary)
{
    FILE *file = fopen(dictionary, "r");
    if (file == NULL)
    {
        return false;
    }

    char word[LENGTH + 1];  // initializing string to store word to be read in fscanf
    while (fscanf(file, "%s", word) != EOF)
    {
        node *n = malloc(sizeof(node));
        indexValue = hash(word);  // calls hash function, stores int in indexValue
        strcpy(n->word, word);  // copies word and stores it in n->word
        n->next = table[indexValue];  // sets pointer to whatever value in table is pointing to
        table[indexValue] = n;

        wordCount++;
    }
    fclose(file);
    return true;
}

// Returns number of words in dictionary if loaded else 0 if not yet loaded
unsigned int size(void)
{
    return wordCount;
}

// Help from Reese 10/13
// Unloads dictionary from memory, returning true if successful else false
bool unload(void)
{
    node *cursor = table[0];

    for (int i = 0; i < N; i++)
    {
        for (cursor = table[i]; cursor != NULL;)
        {
            node *tmp = cursor;
            cursor = cursor->next;
            free(tmp);
        }
    }

    return true;
}
