def main():
    text = input("Text: ")
    letters = letter_counter(text)
    words = word_counter(text) / 100  # averaging per 100 words
    sentences = sentence_counter(text)
    index = round(0.0588 * (letters / words) - 0.296 * (sentences / words) - 15.8)

    if (index < 1):
        print("Before Grade 1")
    elif (index > 16):
        print("Grade 16+")
    else:
        print(f"Grade {index}")

    # DEBUG
    # print(f"Words: {words} Letters: {letters} Sentences: {sentences} Index: {index}\n")


def letter_counter(text):
    total = 0
    for char in text:
        if char.isalpha():
            total += 1
    return total


def word_counter(text):
    total = 0
    for char in text:
        if char == " ":
            total += 1

    return (total + 1)  # adding one for final word


def sentence_counter(text):
    total = 0
    for char in text:
        if char in ['.', '!', '?']:
            total += 1
    return total


if __name__ == "__main__":
    main()
