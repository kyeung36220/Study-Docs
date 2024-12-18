def main():
    name = input("what's your name? ")
    print(hello(name))

def hello(to="world"): #pytest checks return value not side effects
    return f"hello, {to}"

if __name__ == "__main__":
    main()
