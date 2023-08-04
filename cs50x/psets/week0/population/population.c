#include <cs50.h>
#include <stdio.h>
#include <math.h>

int main(void)
{
    // TODO: Prompt for start size
    int start;
    do
    {
        start = get_int("Start size: ");
    }
    while (start < 9);


    // TODO: Prompt for end size
    int end;
    do
    {
        end = get_float("End size: ");
    }
    while (end < start);


    // TODO: Calculate number of years until we reach threshold
int year = 0;
int n = start;
int calc = 0;

// prompt Year: 0 for same input vals
if (start == end){
    printf("Years: 0");
}

do{
    n = round(n + (n / 3) - (n / 4));
    year += 1;
}
while (n < end);
printf("Years: %i", year);

    // TODO: Print number of years
    /*
    return start;
    return end;
    return years;
    */
}





