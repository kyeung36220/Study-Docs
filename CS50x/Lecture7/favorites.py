import csv
from collections import Counter

with open('favorites.csv', 'r') as file:
    reader = csv.DictReader(file)
    counts = Counter()

    for row in reader:
        favorite = row["problem"]
        counts[favorite] += 1

for favorite in counts.most_common(): #count.get orders them by value, and can be reversed
    print(f"{favorite}: {counts[favorite]}")
