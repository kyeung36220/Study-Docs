class Cat:
    MEOWS = 3 #capitalization to show it is a constant by convention

    def meow(self):
        for _ in range(Cat.MEOWS):
            print("meow")

cat = Cat()
cat.meow()
