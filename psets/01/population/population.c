#include <cs50.h>
#include <stdio.h>


int main(void)
{
    // get the star_pop && end_pop values
   int start_pop;
    do
    {
        start_pop = get_int("Start size: ");
    } while (8 >= start_pop);

    int end_pop;
    do
    {
        end_pop = get_int("End size: ");
    } 
    while (start_pop > end_pop);

    // Counting alive pop
    int alive_pop = start_pop + (start_pop / 3) - (start_pop / 4);
    printf("Currently alive: %i \n", alive_pop);

    int time;
    int years;
    do
    {
        int years = time++;
    }
    while(alive_pop > end_pop);

    printf("Years: %i \n", years);
    
    






    return start_pop;
    return end_pop;
    return years;
}









































