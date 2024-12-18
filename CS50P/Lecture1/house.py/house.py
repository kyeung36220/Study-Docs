name = input("What's your name? ")

match name:
    case "Harry" | "Hermoine": # | is or
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case _: # _ catches all
        print("Who?")
