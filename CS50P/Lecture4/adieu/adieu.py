import inflect

p = inflect.engine()
list_of_names = []
number_of_names = 0

while True:
    try:
        text = input("Name: ")
        list_of_names.append(text)
        number_of_names += 1

    except EOFError:
        print("\n")
        if number_of_names == 1:
            print("Adieu, adieu, to", text)
        else:
            print("Adieu, adieu, to", p.join(list_of_names))
        break
