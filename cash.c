#include <cs50.h>
#include <stdio.h>

int main(void)
{   
    float change = 0;
    do
    {
        change = get_float("How much change is owed?\n");
    }
    while (change <= 0);
    
    int coins = 0;
    
    for ( ; change >= 1; change = change - 1)
    {
        coins = coins + 1;
    }
    
    for ( ; change >= .25; change = change - .25)
    {
        coins = coins + 1;
    }
    
    for ( ; change >= .1; change = change - .1)
    {
        coins = coins + 1;
    }
    
    for ( ; change >= .05; change = change - .05)
    {
        coins = coins + 1;
    }
    
    for ( ; change > 0; change = change - .01)
    {
        coins = coins + 1;
    }
    
    printf("%i\n", coins);
}
