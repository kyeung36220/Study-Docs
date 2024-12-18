import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    if matches := re.search(r"(\d?\d)\:?(\d\d)?( [APM][APM])(?: to )(\d?\d)\:?(\d\d)?( [APM][APM])", s):
        hours1, hours2 = int(matches.group(1)), int(matches.group(4))
        mer1, mer2 = matches.group(3).lstrip(), matches.group(6).lstrip()

        if matches.group(2) is None:
            minutes1 = 0
        else:
            minutes1 = int(matches.group(2))

        if matches.group(5) is None:
            minutes2 = 0
        else:
            minutes2 = int(matches.group(5))

        for i in [hours1, hours2]:
            if i < 0 or i > 12:
                raise ValueError
        for i in [minutes1, minutes2]:
            if i < 0 or i >= 60:
                raise ValueError

        if mer1 == "PM" and hours1 < 12:
            hours1 += 12
        elif mer1 == "AM" and hours1 == 12:
            hours1 = 0

        if mer2 == "PM" and hours2 < 12:
                hours2 += 12
        elif mer2 == "AM" and hours2 == 12:
            hours2 = 0

        return f"{hours1:02}:{minutes1:02} to {hours2:02}:{minutes2:02}"

    else:
        raise ValueError



...


if __name__ == "__main__":
    main()
