#include <stdio.h>
#include <cs50.h>

int main(void) {
     string answer = get_string("What's your name? ");
     string a_answer = get_string("What's your age? ");
     printf("Howdy, %s and you're %s!\n", answer, a_answer);
}