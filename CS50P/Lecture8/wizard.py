class Wizard:
    def __init__(self, name)
        if not name:
            raise ValueError("Missing name")
        self.name = name

        ...


class Student(Wizard):
    def __init__(self, name, house):
        super().__init__(name) # super class means parent class and __init__ refering to that parent class's object
        self.house = house

        ...


class Professor(Wizard):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject

        ...

wizard = Wizard("Albus")
student = Student("Harry", "a")
professor = Professor("Severus", "Math")
