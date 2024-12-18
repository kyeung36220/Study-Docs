list = {}


while True:
    try:
        item = input()
        if item in list:
            list[item] += 1
        else:
            list[item] = 1

    except EOFError:
        sorted_list = sorted(list.items())
        print("\n")
        for item, count in sorted_list:
            print(count, item.upper())
        break



    except KeyError:
        print("Not in list")
        break
