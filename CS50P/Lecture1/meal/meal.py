def main():
    time = input("What time is it? ")
    n = convert(time)

    if 7 <= n <= 8:
        print("breakfast time")
    elif 12 <= n <= 13:
        print("lunch time")
    elif 18 <= n <= 19:
        print("dinner time")


def convert(s):
    hours, minutes = s.split(":")
    return float(hours) + (float(minutes) / 60)


if __name__ == "__main__":
    main()
