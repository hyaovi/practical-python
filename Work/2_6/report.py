# report.py
# Exercise 2.5
import csv


def read_price(filename):
    prices = {}
    with open(filename, "rt") as f:
        rows = csv.reader(f)
        for row in rows:
            if len(row) == 2:
                name, price = row
                prices[name] = price

        return prices
