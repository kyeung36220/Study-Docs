class Student: #define class and store methods
    def __init__(self, name, house, spell): #initialization method
        if not name:
            raise ValueError("Missing name")
        if house not in ["a","b","c","d"]:
            raise ValueError("Invalid house")
        self.name = name
        self.house = house
        self.spell = spell

    def __str__(self):
        return f"{self.name} from {self.house}" #accessing class attributes

    def charm(self):
        match self.spell:
            case "stag":
                return "wow, that's a stag jaja"
            case _:
                return "None"

def main():
    student = get_student()
    print(student) #printing class and will go into __str__
    print(student.charm())

def get_student():
    name = input("Name: ") #storing attributes into class
    house = input("House: ")
    spell = input("Spell: ")
    return Student(name, house, spell)


if __name__ == "__main__":
    main()
