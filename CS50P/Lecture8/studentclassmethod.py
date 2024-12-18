class Student: #define class and store methods
    def __init__(self, name, house): #initialization method
        self.name = name
        self.house = house

    def __str__(self):
        return f"{self.name} from {self.house}" #accessing class attribute

    @classmethod
    def get(cls): #can call without instantiating student object first (get functionality)
        name = input("Name: ")
        house = input("House: ")
        return cls(name, house)


def main():
    student = Student.get()
    print(student) #printing class and will go into __str__


if __name__ == "__main__":
    main()
