import csv

students = []

with open ("students.csv") as file:
    reader = csv.reader(file)
    for name, home in reader:
        students.append({"name": name, "home": home})

for student in sorted(students, key=lambda student: student["name"]): #lambda is a substitue for no name function that is used once
    print(f"{student['name']} is from {student['home']}")
