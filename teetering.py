from cs50 import get_int

numbers = []


def main():
    length = get_int("How long is your list? ")
    for i in range(length):
        num = get_int("Number: ")  # gets list input
        numbers.append(num)
    balanceable(numbers)  # calls function balanceable


def balanceable(numbers):
    total = sum(numbers)
    if (total/2 % 1) != 0:  # returns false if sum of list is odd
        print("False")
        return False
    if (inequality(numbers) == False):  # calls inequality function
        print("False")
        return False
    else:
        print("True")
        return True


def inequality(numbers):
    numbersCopy = numbers.copy()
    numbersCopy.remove(max(numbersCopy))
    if max(numbers) > sum(numbersCopy):  # checks if greatest number is greater than the sum of the rest
        return False
    else:
        return True


main()
