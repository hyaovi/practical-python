class Portfolio:
    def __init__(self, holdings) -> None:
        self._holdings = holdings

    def __iter__(self):
        return self._holdings.__iter__()

    @property
    def total_cost(self):
        return sum([s.cost for s in self._holdings])

    def tabulate_shares(self):
        from collections import Counter

        total_shares = Counter()
        for share in self._holdings:
            total_shares[share.name] += share.cost
        return total_shares
