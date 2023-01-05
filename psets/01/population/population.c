#include <cs50.h>
#include <stdio.h>


int main(void)
{
    // global variables
    int start;
    int end;


    size();
    // TODO: Prompt for start size ✅
    // TODO: Prompt for end size ✅
    // get size


}


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


// calculations












































/*
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
*/