from cs50 import get_float

while True:
    dollars = get_float("Change owed: ")
    if dollars > 0:  # runs until dollars is a positive number
        break

change = round(dollars * 100)  # turns dollars into cents
coins = 0  # initializes counter to 0

while True:
    if change >= 25:
        change -= 25
        coins += 1
    if change < 25:
        break  # runs until cannot use any more quarters
while True:
    if change >= 10:
        change -= 10
        coins += 1
    if change < 10:
        break  # runs until cannot use any more dimes
while True:
    if change >= 5:
        change -= 5
        coins += 1
    if change < 5:
        break  # runs until cannot use any more nickels
while True:
    if change >= 1:
        change -= 1
        coins += 1
    if change == 0:
        break  # runs until cannot use any more pennies

print(coins)