from sys import argv, exit
import cs50

if len(argv) != 2:
    print("Correct usage: python import.py *house*")
    exit(1)  # exits program if used incorrectly

db = cs50.SQL("sqlite:///students.db")
roster = db.execute("SELECT first, middle, last, birth FROM students WHERE house = ? ORDER BY last ASC, first ASC;", argv[1])
# selects full name and birth year from table in order for inputted house, stores in roster

for row in roster:  # iterates through roster for inputted house
    if row['middle'] != None:
        print(f"{row['first']} {row['middle']} {row['last']}, born {row['birth']}")  # prints first and last name and year
    else:
        print(f"{row['first']} {row['last']}, born {row['birth']}")  # print first, middle, and last name and year