from cs50 import get_int

numbers = []

def main():
    length = get_int("How long is your list? ")
    for i in range(length):
        num = get_int("Number: ")
        numbers.append(num)
    balanceable(numbers)

def balanceable(numbers):
    total = sum(numbers)
    if (total/2 % 1) != 0:
        print("False")
        return False
    if (inequality(numbers) == False):
        print("False")
        return False
    else:
        print("True")
        return True

def inequality(numbers):
    numbersCopy = numbers.copy()
    numbersCopy.remove(max(numbersCopy))
    if max(numbers) > sum(numbersCopy):
        return False
    else:
        return True

main()