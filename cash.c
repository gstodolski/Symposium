#include <cs50.h>
#include <stdio.h>
#include <math.h>

int main(void)
{   
    float dollars = 0; //initializes variable dollars
    do
    {
        dollars = get_float("How much change is owed?\n"); //asks human for change owed
    }
    while (dollars <= 0); //ensures amount is positive
    
    int change = round(dollars * 100); //rounds dollars and turns it into cents (i.e. 1.40 = 140)
    
    int coins = 0; //initializes coin counter
    
    for (; change >= 25; change = change - 25)  //calculates how many quarters can be used
    {
        coins = coins + 1;
    }
    
    for (; change >= 10; change = change - 10)  //calculates how many dimes can be used
    {
        coins = coins + 1;
    }
    
    for (; change >= 5; change = change - 5)  //calculates how many nickels can be used
    {
        coins = coins + 1;
    }
    
    for (; change > 0; change = change - 1)  //calculates how many pennies can be used
    {
        coins = coins + 1;
    }
    
    printf("Minimum number of coins:\n");
    printf("%i\n", coins); //prints output
}
