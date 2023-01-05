#include <cs50.h>
#include <stdio.h>

int get_start_size(void);

int main(void)
{
    // TODO: Prompt for start size
    int i = get_start_size();

    // TODO: Prompt for end size

    // TODO: Calculate number of years until we reach threshold

    // TODO: Print number of years
}

int get_start_size(void)
{
    int i;
    do
    {
        i = get_int("Starting size: ");
    }
    while (i <= 9);
    return i;
}

