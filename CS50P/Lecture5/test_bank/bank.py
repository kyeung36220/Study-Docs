def main():
    greeting = input("Greeting: ")
    money = value(greeting)
    print("$" + str(money))

def value(s):

    s = str.lower(s).strip()

    if s.startswith("h") == False:
        money = 100
    elif s.startswith("hello") == True:
        money = 0
    else:
        money = 20
    return money

if __name__ == "__main__":
    main()
