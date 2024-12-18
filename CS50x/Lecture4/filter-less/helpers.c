#include "helpers.h"
#include <math.h>

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            int temp =
                round((image[i][j].rgbtBlue + image[i][j].rgbtRed + image[i][j].rgbtGreen) / 3.0);
            image[i][j].rgbtBlue = temp;
            image[i][j].rgbtRed = temp;
            image[i][j].rgbtGreen = temp;
        }
    }
    return;
}

// Convert image to sepia
void sepia(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            int originalRed = image[i][j].rgbtRed;
            int originalGreen = image[i][j].rgbtGreen;
            int originalBlue = image[i][j].rgbtBlue;

            int sepiaRed =
                round(0.393 * originalRed + 0.769 * originalGreen + 0.189 * originalBlue);
            int sepiaGreen =
                round(0.349 * originalRed + 0.686 * originalGreen + 0.168 * originalBlue);
            int sepiaBlue =
                round(0.272 * originalRed + 0.534 * originalGreen + 0.131 * originalBlue);

            image[i][j].rgbtRed = fmin(255, sepiaRed);
            image[i][j].rgbtGreen = fmin(255, sepiaGreen);
            image[i][j].rgbtBlue = fmin(255, sepiaBlue);
        }
    }
    return;
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width / 2; j++)
        {
            RGBTRIPLE temp = image[i][j];
            image[i][j] = image[i][width - j - 1];
            image[i][width - j - 1] = temp;
        }
    }
    return;
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    RGBTRIPLE temp[height][width];

    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            temp[i][j] = image[i][j];
        }
    }

    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            if (i == 0 && j == 0) // top left corner
            {
                image[i][j].rgbtRed = round(
                    (temp[i][j + 1].rgbtRed + temp[i + 1][j].rgbtRed + temp[i + 1][j + 1].rgbtRed) /
                    3.0);
                image[i][j].rgbtGreen = round((temp[i][j + 1].rgbtGreen + temp[i + 1][j].rgbtGreen +
                                               temp[i + 1][j + 1].rgbtGreen) /
                                              3.0);
                image[i][j].rgbtBlue = round((temp[i][j + 1].rgbtBlue + temp[i + 1][j].rgbtBlue +
                                              temp[i + 1][j + 1].rgbtBlue) /
                                             3);
            }
            else if (i == 0 && j == width - 1) // top right corner
            {
                image[i][j].rgbtRed = round(
                    (temp[i][j - 1].rgbtRed + temp[i + 1][j].rgbtRed + temp[i + 1][j - 1].rgbtRed) /
                    3.0);
                image[i][j].rgbtGreen = round((temp[i][j - 1].rgbtGreen + temp[i + 1][j].rgbtGreen +
                                               temp[i + 1][j - 1].rgbtGreen) /
                                              3.0);
                image[i][j].rgbtBlue = round((temp[i][j - 1].rgbtBlue + temp[i + 1][j].rgbtBlue +
                                              temp[i + 1][j - 1].rgbtBlue) /
                                             3.0);
            }
            else if (i == height - 1 && j == 0) // bottom left corner
            {
                image[i][j].rgbtRed = round(
                    (temp[i][j + 1].rgbtRed + temp[i - 1][j].rgbtRed + temp[i - 1][j + 1].rgbtRed) /
                    3.0);
                image[i][j].rgbtGreen = round((temp[i][j + 1].rgbtGreen + temp[i - 1][j].rgbtGreen +
                                               temp[i - 1][j + 1].rgbtGreen) /
                                              3.0);
                image[i][j].rgbtBlue = round((temp[i][j + 1].rgbtBlue + temp[i - 1][j].rgbtBlue +
                                              temp[i - 1][j + 1].rgbtBlue) /
                                             3.0);
            }
            else if (i == height - 1 && j == width - 1) // bottom right corner
            {
                image[i][j].rgbtRed = round(
                    (temp[i][j - 1].rgbtRed + temp[i - 1][j].rgbtRed + temp[i - 1][j - 1].rgbtRed) /
                    3.0);
                image[i][j].rgbtGreen = round((temp[i][j - 1].rgbtGreen + temp[i - 1][j].rgbtGreen +
                                               temp[i - 1][j - 1].rgbtGreen) /
                                              3.0);
                image[i][j].rgbtBlue = round((temp[i][j - 1].rgbtBlue + temp[i - 1][j].rgbtBlue +
                                              temp[i - 1][j - 1].rgbtBlue) /
                                             3.0);
            }
            else if (i == 0) // top row pixels
            {
                image[i][j].rgbtRed = round((temp[i][j - 1].rgbtRed + temp[i + 1][j - 1].rgbtRed +
                                             temp[i + 1][j].rgbtRed + temp[i + 1][j + 1].rgbtRed +
                                             temp[i][j + 1].rgbtRed) /
                                            5.0);
                image[i][j].rgbtGreen =
                    round((temp[i][j - 1].rgbtGreen + temp[i + 1][j - 1].rgbtGreen +
                           temp[i + 1][j].rgbtGreen + temp[i + 1][j + 1].rgbtGreen +
                           temp[i][j + 1].rgbtGreen) /
                          5.0);
                image[i][j].rgbtBlue =
                    round((temp[i][j - 1].rgbtBlue + temp[i + 1][j - 1].rgbtBlue +
                           temp[i + 1][j].rgbtBlue + temp[i + 1][j + 1].rgbtBlue +
                           temp[i][j + 1].rgbtBlue) /
                          5.0);
            }
            else if (i == height - 1) // bottom row pixels
            {
                image[i][j].rgbtRed = round((temp[i][j - 1].rgbtRed + temp[i - 1][j - 1].rgbtRed +
                                             temp[i - 1][j].rgbtRed + temp[i - 1][j + 1].rgbtRed +
                                             temp[i][j + 1].rgbtRed) /
                                            5.0);
                image[i][j].rgbtGreen =
                    round((temp[i][j - 1].rgbtGreen + temp[i - 1][j - 1].rgbtGreen +
                           temp[i - 1][j].rgbtGreen + temp[i - 1][j + 1].rgbtGreen +
                           temp[i][j + 1].rgbtGreen) /
                          5.0);
                image[i][j].rgbtBlue =
                    round((temp[i][j - 1].rgbtBlue + temp[i - 1][j - 1].rgbtBlue +
                           temp[i - 1][j].rgbtBlue + temp[i - 1][j + 1].rgbtBlue +
                           temp[i][j + 1].rgbtBlue) /
                          5.0);
            }
            else if (j == 0) // left side pixels
            {
                image[i][j].rgbtRed = round((temp[i - 1][j].rgbtRed + temp[i - 1][j + 1].rgbtRed +
                                             temp[i][j + 1].rgbtRed + temp[i + 1][j + 1].rgbtRed +
                                             temp[i + 1][j].rgbtRed) /
                                            5.0);
                image[i][j].rgbtGreen =
                    round((temp[i - 1][j].rgbtGreen + temp[i - 1][j + 1].rgbtGreen +
                           temp[i][j + 1].rgbtGreen + temp[i + 1][j + 1].rgbtGreen +
                           temp[i + 1][j].rgbtGreen) /
                          5.0);
                image[i][j].rgbtBlue =
                    round((temp[i - 1][j].rgbtBlue + temp[i - 1][j + 1].rgbtBlue +
                           temp[i][j + 1].rgbtBlue + temp[i + 1][j + 1].rgbtBlue +
                           temp[i + 1][j].rgbtBlue) /
                          5.0);
            }
            else if (j == width - 1) // right side pixels
            {
                image[i][j].rgbtRed = round((temp[i - 1][j].rgbtRed + temp[i - 1][j - 1].rgbtRed +
                                             temp[i][j - 1].rgbtRed + temp[i + 1][j - 1].rgbtRed +
                                             temp[i + 1][j].rgbtRed) /
                                            5.0);
                image[i][j].rgbtGreen =
                    round((temp[i - 1][j].rgbtGreen + temp[i - 1][j - 1].rgbtGreen +
                           temp[i][j - 1].rgbtGreen + temp[i + 1][j - 1].rgbtGreen +
                           temp[i + 1][j].rgbtGreen) /
                          5.0);
                image[i][j].rgbtBlue =
                    round((temp[i - 1][j].rgbtBlue + temp[i - 1][j - 1].rgbtBlue +
                           temp[i][j - 1].rgbtBlue + temp[i + 1][j - 1].rgbtBlue +
                           temp[i + 1][j].rgbtBlue) /
                          5.0);
            }
            else // all other pixels with 8 surrounding pixels
            {
                image[i][j].rgbtRed = round((temp[i - 1][j - 1].rgbtRed + temp[i - 1][j].rgbtRed +
                                             temp[i - 1][j + 1].rgbtRed + temp[i][j + 1].rgbtRed +
                                             temp[i + 1][j + 1].rgbtRed + temp[i + 1][j].rgbtRed +
                                             temp[i + 1][j - 1].rgbtRed + temp[i][j - 1].rgbtRed) /
                                            8);
                image[i][j].rgbtGreen =
                    round((temp[i - 1][j - 1].rgbtGreen + temp[i - 1][j].rgbtGreen +
                           temp[i - 1][j + 1].rgbtGreen + temp[i][j + 1].rgbtGreen +
                           temp[i + 1][j + 1].rgbtGreen + temp[i + 1][j].rgbtGreen +
                           temp[i + 1][j - 1].rgbtGreen + temp[i][j - 1].rgbtGreen) /
                          8);
                image[i][j].rgbtBlue =
                    round((temp[i - 1][j - 1].rgbtBlue + temp[i - 1][j].rgbtBlue +
                           temp[i - 1][j + 1].rgbtBlue + temp[i][j + 1].rgbtBlue +
                           temp[i + 1][j + 1].rgbtBlue + temp[i + 1][j].rgbtBlue +
                           temp[i + 1][j - 1].rgbtBlue + temp[i][j - 1].rgbtBlue) /
                          8);
            }
        }
    }
    return;
}
