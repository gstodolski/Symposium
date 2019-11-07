from sys import argv, exit
import csv
import cs50

if len(argv) != 2:
    print("Correct usage: python import.py *CSV file*")
    exit(1)  # exits program if used incorrectly

open("students.db", "w").close()  # creates database
db = cs50.SQL("sqlite:///students.db")
db.execute("CREATE TABLE students (first TEXT, middle TEXT, last TEXT, house TEXT, birth NUMERIC)")
# creates columns within table students in database
csvFile = csv.DictReader(open(argv[1]))

for row in csvFile:  # iterates through all students
    # split name into first, middle, last
    arr = row['name'].split()
    if len(arr) == 3:
        first = arr[0]
        middle = arr[1]
        last = arr[2]
    elif len(arr) == 2:
        arr.append(None)  # adds 3rd index to array
        arr[1], arr[2] = arr[2], arr[1]  # swaps None from last into middle
        first = arr[0]
        middle = arr[1]
        last = arr[2]
    house = row['house']
    birth = row['birth']
    db.execute("INSERT INTO students VALUES (?, ?, ?, ?, ?)", first, middle, last, house, birth)  # inserts current row into table