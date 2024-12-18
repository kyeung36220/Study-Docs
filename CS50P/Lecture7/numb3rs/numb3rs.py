import re

def main():
    print(validate(input("IPv4 Address: ")))

def validate(ip):
    try:
        number1, number2, number3, number4 = ip.split('.')
    except ValueError:
        return False
    for i in [number1, number2, number3, number4]:
        if int(i) > 250:
            if not re.search(r"^[2][5][0-5]$", i):
                return False
        else:
            if not re.search(r"^[1-2]?[0-9]?[0-9]$", i):
                return False
    return True

if __name__ == "__main__":
    main()
