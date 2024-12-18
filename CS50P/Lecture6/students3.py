import csv

students = []

with open ("students.csv") as file:
    reader = csv.DictReader(file) #csv.reader returns list csv.DictReader return dictionary
    for row in reader:
        students.append({"name": row["name"], "home": row["home"]}) #need to put name,home at start of csv file for this to work with DictReader (can also put row instead)

for student in sorted(students, key=lambda student: student["name"]): #lambda is a substitue for no name function that is used once
    print(f"{student['name']} is from {student['home']}")
