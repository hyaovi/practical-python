from fileparse import parse_csv


# collecting Data


def read_price(filename):
    """read a price CSV file into a dict mapping name to price"""
    return dict(parse_csv(filename=filename, has_headers=False, types=[str, float]))


def read_portfolio(filename):
    """
    Read a portfolio into a list of dictionaries with keys: name, shares, price
    """
    portfolio = parse_csv(
        filename=filename, select=["name", "shares", "price"], types=[str, int, float]
    )
    return portfolio


def make_report(portfolio: list, prices: dict):
    report = []
    for stock in portfolio:
        change = prices[stock["name"]] - stock["price"]
        stock = (
            stock["name"],
            stock["shares"],
            prices[stock["name"]],
            change,
        )
        report.append(stock)
    return report


def print_report(report):
    headers = ("Name", "Shares", "Prices", "Changes")

    print("%10s %10s %10s %10s" % headers)
    print(("_" * 10 + " ") * len(headers))

    for stock in report:
        name, shares, price, change = stock
        print(f"{name:>10s} {shares:>10d} {'$'+f'{price:0.2f}':>10s} {change:>10.2f}")


portfolio = read_portfolio("Data/portfoliodate.csv")
prices = read_price("Data/prices.csv")
report = make_report(portfolio=portfolio, prices=prices)
print_report(report)
