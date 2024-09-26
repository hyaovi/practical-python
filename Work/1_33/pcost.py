# pcost.py
#
# Exercise 1.32
import csv
import sys


def portfolio_cost(filepath: str):
    with open(filepath, "rt") as f:
        rows = csv.reader(f)
        header = next(rows)
        cost = 0
        for row in rows:
            try:
                share = int(row[1])
                price = float(row[2])
                cost = price * share + cost
            except ValueError:
                print(f"Bad data, line :{row}")
        return cost


if len(sys.argv) == 2:
    filepath = sys.argv[1]
else:
    filepath = "Data/portfolio.csv"

cost = portfolio_cost(filepath)
print(f"Total cost : {cost}")
