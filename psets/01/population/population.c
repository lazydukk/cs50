#include <cs50.h>
#include <stdio.h>

int size(void);


int main(void)
{
    // global variables
    // TODO: Prompt for start size ✅
    // TODO: Prompt for end size ✅
    size();
    // TODO: Calculate number of years until we reach threshold
    // TODO: Print number of years
}


// calculations



// get size
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

