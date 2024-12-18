#include <cs50.h>
#include <ctype.h>
#include <math.h>
#include <stdio.h>
#include <string.h>

float letter_counter(string x);
float word_counter(string x);
float sentence_counter(string x);

int main(void)
{
    string text = get_string("Text: ");
    float words = (word_counter(text) + 1) / 100;
    float letters = letter_counter(text);
    float sentences = sentence_counter(text);
    int index = round(0.0588 * (letters / words) - 0.296 * (sentences / words) - 15.8);
    if (index < 1)
    {
        printf("Before Grade 1\n");
    }
    else if (index > 16)
    {
        printf("Grade 16+\n");
    }
    else
    {
        printf("Grade %d\n", index);
    }
    // printf("Words: %f Letters: %f Sentences: %f Index: %d\n", words, letters, sentences, index);
}

float letter_counter(string x)
{
    int total = 0;
    for (int i = 0; i < strlen(x); i++)
    {
        if isalpha (x[i])
        {
            total++;
        }
    }
    return total;
}

float word_counter(string x)
{
    int total = 0;
    for (int i = 0; i < strlen(x); i++)
    {
        if isblank (x[i])
        {
            total++;
        }
    }
    return total;
}

float sentence_counter(string x)
{
    int total = 0;
    for (int i = 0; i < strlen(x); i++)
    {
        if (x[i] == '.' || x[i] == '!' || x[i] == '?')
        {
            total++;
        }
    }
    return total;
}
