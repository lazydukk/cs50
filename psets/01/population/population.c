#include <cs50.h>
#include <stdio.h>

int size(void);


int main(void)
{
    // TODO: Prompt for start size
    size();
    // TODO: Prompt for end size
    // TODO: Calculate number of years until we reach threshold

    // TODO: Print number of years
}

// get start number



int size(void)
{
    int start;
    do
    {
        start = get_int("Start size: ");
    } while (8 >= start);

    int end;
    do
    {
        end = get_int("End size: ");
    } 
    while (start > end);

    return start;
    return end;
}
