import validators

def main():
    try:
        is_email = validators.email(input("What's your email address? "))
        if is_email == True:
            print("Valid")
        else:
            print("Invalid")
    except ValidationError:
        print("Invalid")

if __name__ == "__main__":
    main()
