#!/usr/bin/env python3

# pcost.py
#
# Exercise 3.15

import sys
import report


def portfolio_cost(filepath: str):
    portfolio_report = report.read_portfolio(filename=filepath)
    cost = sum([item["shares"] * item["price"] for item in portfolio_report])
    return cost


def main(argv):
    pcost_module_name, portfolio_filename = argv
    if "pcost.py" in pcost_module_name:
        cost = portfolio_cost(portfolio_filename)
        print(f"Total cost : {cost}")


if len(sys.argv) == 2:
    main(sys.argv)
