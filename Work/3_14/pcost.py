# pcost.py
#
# Exercise 1.32
import csv
import sys
import report


def portfolio_cost(filepath: str):
    cost = report.read_portfolio(filename=filepath)
    return cost


if len(sys.argv) == 2:
    filepath = sys.argv[1]
else:
    filepath = "Data/portfolio.csv"

cost = portfolio_cost(filepath)
print(f"Total cost : {cost}")
