import csv
import sys

def main():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    elif sys.argv[1].endswith(".csv") == False:
        sys.exit("Argument 1 not CSV file")
    elif sys.argv[2].endswith(".csv") == False:
        sys.exit("Argument 2 not CSV file")

    try:
        with open (sys.argv[1], "r") as file, open(sys.argv[2], "w", newline = '') as adjusted:
            reader = csv.DictReader(file, fieldnames=["name", "house"])
            writer = csv.DictWriter(adjusted, fieldnames=["first", "last", "house"]) #assigning labels for new file

            writer.writeheader() #making header line

            next(reader) #skipping header line

            for row in reader:
                last_name, first_name = row["name"].split(", ") #spliiting original name into two parts for new file
                writer.writerow({
                    "first": first_name,
                    "last" : last_name,
                    "house" : row["house"]
                })


    except FileNotFoundError:
        sys.exit(f"Could not read {sys.argv[1]}")

main()
