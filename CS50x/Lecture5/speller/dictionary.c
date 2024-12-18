// Implements a dictionary's functionality
#include <cs50.h>
#include <ctype.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include "dictionary.h"

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
} node;

// TODO: Choose number of buckets in hash table
const unsigned int HASH_MAX = 26;

// Hash table
node *table[HASH_MAX];

// Word Counter
unsigned int word_count = 0;

// Returns true if word is in dictionary, else false
bool check(const char *word)
{
    char *adjusted_word = malloc(strlen(word) + 1);
    strcpy(adjusted_word, word);
    for (int i = 0; i < strlen(adjusted_word); i++)
    {
        if (isalpha(adjusted_word[i]) != 0)
        {
            adjusted_word[i] = tolower(adjusted_word[i]);
        }
    }

    int hash_number = hash(adjusted_word);
    for (node *ptr = table[hash_number]; ptr != NULL; ptr = ptr->next)
    {
        if (strcmp(ptr->word, adjusted_word) == 0)
        {
            free(adjusted_word);
            return true;
        }
    }
    free(adjusted_word);
    return false;
}

// Hashes word to a number
unsigned int hash(const char *word)
{
    return word[0] % HASH_MAX;
}

// Loads dictionary into memory, returning true if successful, else false
bool load(const char *dictionary)
{
    // Open the dictionary file
    FILE *source = fopen(dictionary, "r");
    if (source == NULL)
    {
        printf("Could not open %s.\n", dictionary);
        return false;
    }

    // Read each word in the file
    char word[LENGTH + 1];

    while (fscanf(source, "%s", word) == 1)
    {
        // Add each word to the hash table
        node *n = malloc(sizeof(node));
        strcpy(n->word, word);
        int hash_number = hash(word);
        word_count += 1;
        if (table[hash_number] == NULL)
        {
            table[hash_number] = n;
            n->next = NULL;
        }
        else
        {
            for (node *ptr = table[hash_number]; ptr != NULL; ptr = ptr->next)
            {
                // If at end of list
                if (ptr->next == NULL)
                {
                    // Append node
                    ptr->next = n;
                    break;
                }
            }
        }
    }
    // Close the dictionary file
    fclose(source);
    return true;
}
// Returns number of words in dictionary if loaded, else 0 if not yet loaded
unsigned int size(void)
{
    return word_count;
}

// Unloads dictionary from memory, returning true if successful, else false
bool unload(void)
{
    for (int i = 0; i < HASH_MAX; i++)
    {
        node *cursor = table[i];

        while (cursor != NULL)
        {
            node *temp = cursor;
            cursor = cursor->next;
            free(temp);
        }
        free(cursor);
    }
    return true;
}
