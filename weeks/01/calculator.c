#include <stdio.h>
#include <cs50.h>

int main(void)
{
    // Add two numbers; long means to get more numbers and %li is the format for it

    long x = get_long("Whats x: ");
    long y = get_long("Whats y: ");

    printf("%li\n", x + y);

    // Floats

    float i = get_float("Whats i: ");
    float j = get_float("Whats j: ");

    printf("%.20f\n", i / j);
}