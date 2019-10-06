#include "helpers.h"
#include <math.h>
#include <stdio.h>

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            float average = 0;
            average = (image[i][j].rgbtRed + image[i][j].rgbtGreen + image[i][j].rgbtBlue) / 3.000;
            image[i][j].rgbtRed = round(average);
            image[i][j].rgbtGreen = round(average);
            image[i][j].rgbtBlue = round(average);
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
            float sepiaRed = .393 * image[i][j].rgbtRed + .769 * image[i][j].rgbtGreen + .189 * image[i][j].rgbtBlue;
            float sepiaGreen = .349 * image[i][j].rgbtRed + .686 * image[i][j].rgbtGreen + .168 * image[i][j].rgbtBlue;
            float sepiaBlue = .272 * image[i][j].rgbtRed + .534 * image[i][j].rgbtGreen + .131 * image[i][j].rgbtBlue;

            if (sepiaRed > 255)
            {
                sepiaRed = 255;
            }
            if (sepiaGreen > 255)
            {
                sepiaGreen = 255;
            }
            if (sepiaBlue > 255)
            {
                sepiaBlue = 255;
            }

            image[i][j].rgbtRed = round(sepiaRed);
            image[i][j].rgbtBlue = round(sepiaBlue);
            image[i][j].rgbtGreen = round(sepiaGreen);
        }
    }

    return;
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {

        }
    }
    return;
}

// Blur image
// Walkthrough with Reese and Max 10/6
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    RGBTRIPLE newImage[height][width];

    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            int rtotal = 0;
            int gtotal = 0;
            int btotal = 0;
            int ptotal = 0;

            for (int k = i - 1; k <= i + 1; k++)  //row
            {
                for (int l = j - 1; l <= j + 1; l++)  //column
                {
                    if (0 <= k && k < width && 0 <= l && l < height)
                    {
                        ptotal++;
                        rtotal += image[k][l].rgbtRed;
                        gtotal += image[k][l].rgbtGreen;
                        btotal += image[k][l].rgbtBlue;
                    }
                }
            }

            int averageRed = round(rtotal / (ptotal * 1.0));
            int averageGreen = round(gtotal / (ptotal * 1.0));
            int averageBlue = round(btotal / (ptotal * 1.0));

            newImage[i][j].rgbtRed = averageRed;
            newImage[i][j].rgbtGreen = averageGreen;
            newImage[i][j].rgbtBlue = averageBlue;

        }
    }

    for (int x = 0; x < height; x++)
    {
        for (int y = 0; y < width; y++)
        {
            image[x][y].rgbtRed = newImage[x][y].rgbtRed;
            image[x][y].rgbtGreen = newImage[x][y].rgbtGreen;
            image[x][y].rgbtBlue = newImage[x][y].rgbtBlue;
        }
    }

    return;
}
