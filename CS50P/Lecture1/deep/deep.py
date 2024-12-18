text = str.lower(input("What is the Great Question of Life, the Universe and Everything?")).strip()

match text:
    case "42" | "forty-two" | "forty two":
        print("Yes")
    case _:
        print("No")
