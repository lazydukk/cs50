#include <stdio.h>
#include <cs50.h>

// To show that the function is declared 
int get_size(void);
void print_grid(int size);


int main(void) 
{
    int n = get_size();

    print_grid(n);
}


// Custom functions
int get_size(void)
{
    int n;
    do 
    {
        n = get_int("Size: ");
    }
    while (n < 1);

    return n;
}

void print_grid(int size)
{
    for (int i = 0; i < size; i++)
    {
        for (int j = 0; j < size; j++)
        {
            printf("#");
        }
        printf("\n");
    }
}