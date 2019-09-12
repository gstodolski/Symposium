#include <cs50.h>
#include <stdio.h>
#include <math.h>

int main(void)
{   
    float dollars = 0;
    do
    {
        dollars = get_float("How much change is owed?\n");
    }
    while (dollars <= 0); //ensures 
    
    int change = round(dollars * 100);
    
    int coins = 0; //initializes coin counter
    
    for ( ; change >= 25; change = change - 25)
    {
        coins = coins + 1;
    }
    
    for ( ; change >= 10; change = change - 10)
    {
        coins = coins + 1;
    }
    
    for ( ; change >= 5; change = change - 5)
    {
        coins = coins + 1;
    }
    
    for ( ; change > 0; change = change - 1)
    {
        coins = coins + 1;
    }
    
    printf("%i\n", coins);
}
