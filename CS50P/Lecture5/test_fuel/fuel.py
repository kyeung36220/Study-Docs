def main():
    frac = input("Fraction: ")
    perc = convert(frac)
    amount = gauge(perc)
    print(amount)


def convert(fraction):
    x, y = fraction.split('/')
    if y == "0":
        raise ZeroDivisionError
    elif int(x) > int(y) or x.isnumeric() == False or y.isnumeric() == False:
        raise ValueError
    elif int(x) <= int(y):
        fuel = round(int(x) / int(y) * 100)
    return fuel


def gauge(percentage):
    if percentage <= 1:
        s = "E"
    elif percentage >= 99:
        s = "F"
    else:
        s = (str(percentage) + "%")
    return s

if __name__ == "__main__":
    main()
