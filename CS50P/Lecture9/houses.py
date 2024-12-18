students = [
    {"name": "Hermoine", "house": "Gryff"},
    {"name": "Draco", "house": "Slytherin"}
]

houses = set()
for student in students:
    houses.add(student["house"])

for house in sorted(houses):
    print(house)
