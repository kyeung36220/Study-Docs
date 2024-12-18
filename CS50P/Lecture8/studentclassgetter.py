class Student: #define class and store methods
    def __init__(self, name, house): #initialization method
        self.name = name
        self.house = house

    def __str__(self):
        return f"{self.name} from {self.house}" #accessing class attribute

    #Getter & Setter to filter code and do things with it
    @property
    def house(self):
        return self._house

    #Setter which tells code that you will check house
    @house.setter
    def house(self, house):
        if house not in ["a", "b", "c", "d"]:
            raise ValueError("Invalid house")
        self._house = house

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self,name):
        if not name:
            raise ValueError("Missing name")
        self._name = name

def main():
    student = get_student()
    print(student) #printing class and will go into __str__

def get_student():
    name = input("Name: ") #storing attributes into class
    house = input("House: ")
    return Student(name, house) #calls student constructor


if __name__ == "__main__":
    main()
