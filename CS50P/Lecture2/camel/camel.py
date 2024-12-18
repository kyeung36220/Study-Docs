def main():
    text = input("camelCase: ")
    for c in text:
        if c.islower() == True:
            print(c, sep="", end="")
        elif c.isupper() == True:
            print("_", str.lower(c), sep="", end="")
    print()

main()
