import sys

def main():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    elif sys.argv[1].endswith(".py") == False:
        sys.exit("Not a Python file")

    try:
        lines = 0
        with open(sys.argv[1]) as file:
            for line in file:
                line = line.strip()
                if line and line.startswith("#") == False:
                    lines += 1
        print(lines)

    except FileNotFoundError:
        sys.exit("File does not exist")

main()
