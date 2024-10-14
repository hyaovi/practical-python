#!/usr/bin/env python3


import report


def portfolio_cost(filepath: str):
    portfolio_report = report.read_portfolio(filename=filepath)
    cost = sum([stock.cost() for stock in portfolio_report])
    return cost


def main(argv):
    if len(argv) != 2:
        raise SystemExit("incorrect amount of arguments provided: %s" % argv)
    portfolio_filename = argv[1]
    cost = portfolio_cost(portfolio_filename)
    print(f"Total cost : {cost}")


if __name__ == "__main__":
    import sys

    main(sys.argv)
