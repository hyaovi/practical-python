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


def read_portfolio(filename):
    portfolio = []
    with open(filename, "rt") as f:
        rows = csv.reader(f)
        header = next(rows)
        for row in rows:
            holding = {
                header[0]: row[0],
                header[1]: int(row[1]),
                header[2]: float(row[2]),
            }
            portfolio.append(holding)
        return portfolio


portfolio = read_portfolio("Data/portfolio.csv")
prices = read_price("Data/prices.csv")

old_cost = 0
new_cost = 0

for holding in portfolio:
    old_cost += holding["shares"] * holding["price"]
    new_cost += holding["shares"] * prices[holding["name"]]

print(f"cost: {old_cost},  new cost: {new_cost},  gain: {new_cost-old_cost}")
