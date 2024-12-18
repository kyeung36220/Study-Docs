def main():
    student = get_student()
    print(f"{student[0]} from {student[1]}")

def get_student():
    name = input("Name: ")
    house = input("House: ")
    return (name, house) #tuple has parenthesis and list has sqwuare brackets, tuples cannot be changed


if __name__ == "__main__":
    main()
