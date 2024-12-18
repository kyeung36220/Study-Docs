
while True:
    try:
        fraction = input("Fraction: ")
        x, y = fraction.split('/')
        if int(x) <= int(y):
            fuel = round(int(x) / int(y) * 100)
            if fuel <= 1:
                print("E")
            elif fuel >= 99:
                print("F")
            else:
                print(fuel, "%", sep="")
            break
        else:
            pass
    except ValueError:
        pass
    except ZeroDivisionError:
        pass


