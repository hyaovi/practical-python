# report.py
# Exercise 2.5
import csv


def read_price(filename):
    prices = {}
    with open(filename, "rt") as f:
        rows = csv.reader(f)
        for row in rows:
            try:
                name, price = row
                prices[name] = float(price)
            except ValueError:
                pass
        return prices
