class Package:
    def __init__(self, number, sender, recepient, weight): #instance class
        self.number = number
        self.sender = sender #instance variable
        self.recepient = recepient
        self.weight = weight

    def __str__(self):
        return f"Package {self.number}: {self.sender} to {self.recepient}, {self.weight}kg"

    def calculate_cost(self, cost_per_kg):
        return cost_per_kg * self.weight


def main():
    #packages = ["Packages 1: Alice to Bob, 10kg, Package 2: Bob to Charlie, 5kg"]
    packages = [
        Package(number=1, sender="Alice", recepient="Bob", weight=10),
        Package(number=2, sender="Bob", recepient="Charlie", weight=5)
    ]
    for package in packages:
        print(f"{package} costs ${package.calculate_cost(cost_per_kg=2)}")

main()
