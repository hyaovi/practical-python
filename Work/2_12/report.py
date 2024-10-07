import csv

# collecting Data


def read_price(filename):
    """read a price CSV file into a dict mapping name to price"""
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


def read_portfolio(filename):
    """
    Read a portfolio into a list of dictionaries with keys: name, shares, price
    """
    portfolio = []
    with open(filename, "rt") as f:
        rows = csv.reader(f)
        header = next(rows)
        for row in rows:
            stock = {
                "name": row[0],
                "shares": int(row[1]),
                "price": float(row[2]),
            }
            portfolio.append(stock)
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
        # price_with_unit = "$" + f"{price:0.2f}"
        print(f"{name:>10s} {shares:>10d} {'$'+f'{price:0.2f}':>10s} {change:>10.2f}")


portfolio = read_portfolio("Data/portfolio.csv")
prices = read_price("Data/prices.csv")
report = make_report(portfolio=portfolio, prices=prices)
print_report(report)