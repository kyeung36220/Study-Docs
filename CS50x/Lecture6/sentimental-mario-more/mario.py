
while True:
    height = input("Height: ")
    if height.isdigit() == True and 0 < int(height) <= 8:
        height = int(height)
        break

spaces = height - 1
counter = 1
for i in range(height):
    print(" " * spaces, end="")
    print("#" * counter, end="")
    print("  ", end="")
    print("#" * counter, end="")
    print()
    counter += 1
    spaces -= 1
