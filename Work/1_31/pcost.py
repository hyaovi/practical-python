# pcost.py
#
# Exercise 1.31
def portfolio_cost(filename):
    cost = 0
    with open(filename, "rt") as f:
        header = next(f)
        for line in f:
            try:
                row = line.split(",")
                share = int(row[1])
                price = float(row[2])
                cost = cost + price * share
            except ValueError:
                print(f"Bad data input: {line}")

    print(f"Total cost {round(cost,2)}")


portfolio_cost("Data/portfolio.csv")
