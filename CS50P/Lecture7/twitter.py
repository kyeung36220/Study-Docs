import re
#there is also function called .replace and .removeprefix i think with string functions

url = input("URL: ").strip()

username = re.sub(r"^(https?://)?(www\.)?twitter\.com/", "" , url)

print(f"Username: {username}")
