import csv
import sys


def main():

    # TODO: Check for command-line usage
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    elif sys.argv[1].endswith(".csv") == False:
        sys.exit("File 1 not CSV file")
    elif sys.argv[2].endswith(".txt") == False:
        sys.exit("File 2 not TXT file")

    # TODO: Read database file into a variable
    with open(sys.argv[1]) as file:
        reader = csv.DictReader(file)
        fields = reader.fieldnames
        if fields[0] == 'name':
            fields.remove('name')

    # TODO: Read DNA sequence file into a variable
    f = open(sys.argv[2])
    sequence = f.read()

    # TODO: Find longest match of each STR in DNA sequence
    match_index = {}
    for subsequence in fields:
        match_index[subsequence] = longest_match(sequence, subsequence)

    # TODO: Check database for matching profiles
    with open(sys.argv[1]) as file:
        reader = csv.DictReader(file)
        for row in reader:
            counter = 0
            for subsequence in match_index:
                if int(row[subsequence]) == int(match_index[subsequence]):
                    counter += 1
                    if counter == len(match_index):
                        sys.exit(row['name'])
    print("No match")
    return


def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""

    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):

        # Initialize count of consecutive runs
        count = 0

        # Check for a subsequence match in a "substring" (a subset of characters) within sequence
        # If a match, move substring to next potential match in sequence
        # Continue moving substring and checking for matches until out of consecutive matches
        while True:

            # Adjust substring start and end
            start = i + count * subsequence_length
            end = start + subsequence_length

            # If there is a match in the substring
            if sequence[start:end] == subsequence:
                count += 1

            # If there is no match in the substring
            else:
                break

        # Update most consecutive matches found
        longest_run = max(longest_run, count)

    # After checking for runs at each character in seqeuence, return longest run found
    return longest_run


main()
