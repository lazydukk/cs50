#include <stdio.h>
#include <cs50.h>

int main(void) {
     string first_name = get_string("What's your name? ");
     string second_name = get_string("What's your second name? ");
     printf("Howdy, %s %s\n", first_name, second_name);
}