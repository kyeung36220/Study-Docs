def main():
    text = str(input("Text: "))
    converted_text = shorten(text)
    print(converted_text)

def shorten(word):
    string = ""
    for c in str(word):
        if str(c).lower() in {'a', 'e', 'i', 'o', 'u'}:
            pass
        else:
            string += str(c)
    return string


if __name__ == "__main__":
    main()
