
def main():
    name = input("What's your name? ")#.strip().title() #removes whitespace and capitalize first letter of each word
    hello(name)

def hello(to="world"): # in case no argument then world will be put
    print("hello", to)

main()
