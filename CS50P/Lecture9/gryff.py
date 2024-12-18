students = [
    {"name": "Hermoine", "house": "Gryff"},
    {"name": "Draco", "house": "Slytherin"}
]


gryffs = [
    student["name"] for student in students if student["house"] == "Gryff"
]

for gryff in sorted(gryffs):
    print(gryff)
