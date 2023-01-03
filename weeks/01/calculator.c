#include <stdio.h>
#include <cs50.h>

int main(void)
{
    // Add two numbers

    int x = get_int("Whats x: ");
    int y = get_int("Whats y: ");

    printf("%i\n", x + y);
}