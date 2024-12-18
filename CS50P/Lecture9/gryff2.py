students = ["Hermoine", "Harry", "Ron"]


gryffs = {student: "Gryffindor" for student in students}

print(gryffs)

for i, student in enumerate(students):
    print(i+1, student)
