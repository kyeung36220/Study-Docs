months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

def main():
    while True:
        date = input("Date: ").strip()
        if validity_checker(date) == True:
            break
    date_finder(date)


def validity_checker(s):
    try:
        if s[0].isnumeric() == True:
            month, day, year = s.split('/')
            if 0 > int(month) or int(month) > 12:
                return False
            elif int(day) > 31 or int(day) < 0:
                return False
            else:
                return True

        elif s[0].isalpha() == True:
            if s[-6] != (','):
                return False
            month, day, year = s.split(' ')
            if 0 > int(day.strip(',')) or int(day.strip(',')) > 31:
                return False
            elif month.title() in months:
                return True
            else:
                return False
    except ValueError:
        return False
    except IndexError:
        return False


def date_finder(s):
    if s[0].isnumeric() == True:
        month, day, year = s.split('/')
        if int(day) < 10:
            day = f"{int(day):02}"
        if int(month) < 10:
            month = f"{int(month):02}"
        print(year, month, day, sep="-")

    elif s[0].isalpha() == True:
        month, day, year = s.split(' ')
        day = day.strip(',')
        if int(day) < 10:
            day = f"{int(day):02}"
        month = months.index(month.title()) + 1
        if int(month) < 10:
            month = f"{int(month):02}"
        print(year, month, day, sep="-")

main()
