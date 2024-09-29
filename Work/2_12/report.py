import csv

# collecting Data


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


def read_portfolio(filename):
    portfolio = []
    with open(filename, "rt") as f:
        rows = csv.reader(f)
        header = next(rows)
        for row in rows:
            stock = {
                header[0]: row[0],
                header[1]: int(row[1]),
                header[2]: float(row[2]),
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
    print(
        "{name:>10s} {shares:>10s} {price:>10s} {change:>10s}".format(
            name="Name", shares="Shares", price="Prices", change="Changes"
        )
    )
    print("{n:_>10s} {n:_>10s} {n:_>10s} {n:_>10s}".format(n="_"))

    for stock in report:
        name, shares, price, change = stock
        # price_with_unit = "$" + f"{price:0.2f}"
        print(f"{name:>10s} {shares:>10d} {'$'+f'{price:0.2f}':>10s} {change:>10.2f}")


portfolio = read_portfolio("Data/portfolio.csv")
prices = read_price("Data/prices.csv")
report = make_report(portfolio=portfolio, prices=prices)
print_report(report)
