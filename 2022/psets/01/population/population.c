#include <cs50.h>
#include <stdio.h>


int main(void)
{
    // get the star_pop && end_pop values
    int start;
    int end;
    int year = 0;

    // start population number
    do
    {
        start = get_int("Start size: ");
    } 
    while (8 >= start);

    // end population number
    do
    {
        end = get_int("End size: ");
    } 
    while (start > end);

    // time that will take
    do 
    {
        start = start + (start / 3) - (start / 4);
        year++;
    }
    while (start < end);
    
    // displaying out 
    printf("Years: %i \n", year);

    return start;
    return end;
    return year;
}










































