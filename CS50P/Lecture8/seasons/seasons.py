from datetime import date
import sys
import inflect

def main():
    dob = input("Date of Birth: ")
    total_minutes = get_total(dob)
    print(total_minutes)

def get_total(s):
    try:
        total_days = (date.today() - date.fromisoformat(s)).days
    except Exception:
        sys.exit("Invalid Date")

    return f"{str.capitalize(inflect.engine().number_to_words(total_days * 24 * 60)).replace(" and ", " ")} minutes"

if __name__ == "__main__":
    main()
