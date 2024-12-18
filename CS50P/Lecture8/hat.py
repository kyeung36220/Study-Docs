import random

class Hat:

    houses = ["a", "b", "c", "d"]

    @classmethod
    def sort(cls, name):
        print(name, "is in", random.choice(cls.houses)) #instace variable -> class variable


#hat = Hat() not needed if class variable, class is THE hat when instances can be multiple hats
Hat.sort("Harry")
