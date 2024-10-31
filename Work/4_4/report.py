#!/usr/bin/env python3
from fileparse import parse_csv
from stock import Stock


def read_price(filename):
    """read a price CSV file into a dict mapping name to price"""
    with open(filename, "r") as f:
        return dict(parse_csv(lines=f, has_headers=False, types=[str, float]))


def read_portfolio(filename):
    """
    Read a portfolio into a list of dictionaries with keys: name, shares, price
    """
    with open(filename, "rt") as f:
        portfolio = parse_csv(
            lines=f, select=["name", "shares", "price"], types=[str, int, float]
        )
        portfolio = [Stock(**s) for s in portfolio]
        return portfolio


def make_report(portfolio, prices):
    report = []
    for stock in portfolio:
        change = prices[stock.name] - stock.price
        stock_report = (
            stock.name,
            stock.shares,
            prices[stock.name],
            change,
        )
        report.append(stock_report)
    return report


def print_report(report):
    """Print report  by iterating thought report list"""
    headers = ("Name", "Shares", "Prices", "Changes")

    print("%10s %10s %10s %10s" % headers)
    print(("_" * 10 + " ") * len(headers))

    for stock in report:
        name, shares, price, change = stock
        print(f"{name:>10s} {shares:>10d} {'$'+f'{price:0.2f}':>10s} {change:>10.2f}")


def report_portfolio(portfolio_filename, price_filename):
    portfolio = read_portfolio(portfolio_filename)
    prices = read_price(price_filename)
    report = make_report(portfolio=portfolio, prices=prices)
    print_report(report)


def main(argv):
    if len(argv) != 3:
        raise SystemExit("exist %s module" % argv[1:])
    report_portfolio(argv[1], argv[2])


if __name__ == "__main__":
    import sys

    main(sys.argv)
