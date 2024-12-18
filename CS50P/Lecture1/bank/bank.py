greeting = str.lower(input("Greeting: ")).strip()

if greeting.startswith("h") == False:
    print("$100")
elif greeting.startswith("hello") == True:
    print("$0")
else:
    print("$20")

