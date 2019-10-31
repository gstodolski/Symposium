from cs50 import get_int

while True:
    n = get_int("Height: ")
    if n >= 1 and n <= 8:
        break  # exits loop if n is between 1 and 8, inclusive

for i in range(n):
    for j in range (n - i - 1):  # prints spaces before pyramid
        print(" ", end="")

    for k in range(i + 1):  # loop that prints first pyramid
        print("#", end="")

    print("  ", end="")  # prints gap between pyramids

    for l in range(i + 1):  # loop that prints second pyramid
        print("#", end="")

    print("")  # new line