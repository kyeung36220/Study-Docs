import random

while True:
    try:
        level = int(input("Level: "))
        if level > 1:
            break
    except Exception:
        pass

number = random.randrange(1, level, 1)

while True:
    try:
        guess = int(input("Guess: "))

        if guess > number:
            print("Too large!")
        elif guess < number:
            print("Too small!")
        else:
            print("Just right!")
            break
    except Exception:
        pass
