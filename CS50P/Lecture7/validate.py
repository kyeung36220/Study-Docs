import re

email = input("What's your email? ").strip()

if re.search(r"^(\w|\.)+@(\w+\.)?\w+\.(edu|net|com|org)$", email, re.IGNORECASE): #[a-zA-Z0-9_] = \w | [^@] = anything but inside brackets
    print("Valid")
else:
    print("Invalid")
