from sys import argv, exit
import csv
import re

if len(argv) != 3:
    print("Correct usage: python dna.py *CSV file* *DNA file*")
    exit(1)  # exits program if used incorrectly

csvFile = open(argv[1])  # opens and reads files
dnaFile = csv.DictReader(csvFile)
file = open(argv[2], 'r')
sequence = file.read()

d = {}

for STR in dnaFile.fieldnames[1:]:
    maxLength = 0
    for i in range(len(sequence)):
        length = 0
        while True:
            if sequence[i:(i+len(STR))] == STR:  # reads length of STR
                length += 1
                i += len(STR)
            else:
                break
        if length > maxLength:
            maxLength = length
    d[str(STR)] = maxLength  # adds lengths to dict

strCount = len(d)  # total amount of strings to be compared with counter

for row in dnaFile:
    counter = 0  # resets counter with each row
    for STR in dnaFile.fieldnames[1:]:
        valueDNA = int(row[STR])
        valueDict = d[STR]
        if valueDNA == valueDict:
            counter += 1
    if counter == strCount:  # checks if all STR counts are matches
        print(row['name'])
        exit(2)  # ends program if match is found
print("No match")  # prints if a name is not printed