students = [
    {"name": "Hermoine", "house": "Ahouse", "pet": "otter"},
    {"name": "Harry", "house": "Bhouse", "pet": "dog"},
    {"name": "John", "house": "Chouse", "pet": "capybara"},
    {"name": "Dick", "house": "Dhouse", "pet": None}
]

for student in students:
    print(student["name"], student["house"], student["pet"], sep=", ")
