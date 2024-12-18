from PIL import Image, ImageOps
import sys

def main():
    check_files(sys.argv)

    try:
        with Image.open(sys.argv[1]) as input, Image.open("shirt.png") as shirt:
            input = ImageOps.fit(input, shirt.size)
            input.paste(shirt, shirt)
            input.save(sys.argv[2])

    except FileNotFoundError:
        sys.exit("File does not exist")


def check_files(x):
    if len(x) < 3:
        sys.exit("Too few command-line arguments")
    elif len(x) > 3:
        sys.exit("Too many command-line arguments")
    elif x[1][-3:] != x[2][-3:]:
        sys.exit("Input and output have different extensions")
    else:
        for file_name in [".jpg", ".jpeg", ".png"]:
            if x[1].endswith(file_name):
                return True
        sys.exit("Invalid Input")

if __name__ == "__main__":
    main()
