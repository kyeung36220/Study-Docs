import sys
import random
from pyfiglet import Figlet

figlet = Figlet()

try:
    if len(sys.argv) == 1:
        text = input("Input: ")
        random_font = random.choice(figlet.getFonts())
        figlet.setFont(font=random_font)
        print(figlet.renderText(text))

    elif len(sys.argv) == 3:
        if sys.argv[1] == "-f" or sys.argv[1] == "--font":
            figlet.setFont(font=sys.argv[2])
            text = input("Input: ")
            print(figlet.renderText(text))
        else:
            sys.exit("Invalid second argument")

    else:
        sys.exit("Invalid length")

except Exception:
    sys.exit("Invalid error")
