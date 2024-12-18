students = [
    {"name": "Hermoine", "house": "Gryff"},
    {"name": "Draco", "house": "Slytherin"},
]


def is_gryff(s):
    return s["house"] == Gryff


gryffs = filter(is_gryff, students)

for gryff in gryffs:
    print(gryff["name"])
