from cs50 import get_float

while True:
    dollars = get_float("Change owed: ")
    if dollars > 0:
        break

change = round(dollars * 100)
coins = 0;

while True:
    if change >= 25:
        change -= 25
        coins += 1
    if change < 25:
        break
while True:
    if change >= 10:
        change -= 10
        coins += 1
    if change < 10:
        break
while True:
    if change >= 5:
        change -= 5
        coins += 1
    if change < 5:
        break
while True:
    if change >= 1:
        change -= 1
        coins += 1
    if change == 0:
        break

print(coins)