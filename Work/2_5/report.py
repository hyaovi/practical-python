# report.py
# Exercise 2.5
import csv


def read_portfolio(filename):
    portfolio = []
    with open(filename, "rt") as f:
        rows = csv.reader(f)
        header = next(rows)
        for row in rows:
            holding = {
                (header[0], row[0]),
                (header[1], int(row[1])),
                (header[2], float(row[2])),
            }
            portfolio.append(holding)
        return portfolio
