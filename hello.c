#include <cs50.h>
#include <stdio.h>

int main(void)
{
    string name = get_string("What's your name?\n"); //asks human for name, saved in string "name"
    printf("hello, %s\n", name); //prints "hello, *name*"
}
