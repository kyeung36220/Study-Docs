import re
#there is also function called .replace and .removeprefix i think with string functions

url = input("URL: ").strip()

if matches := re.search(r"^(?:https?://)?(?:www\.)?twitter\.com/(\w+)$", url, re.IGNORECASE):
    print(f"Username:", matches.group(1))
