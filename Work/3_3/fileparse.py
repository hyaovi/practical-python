# fileparse.py
#
# Exercise 3.3
import csv


def parse_csv(filename):
    """reads csv file into a dictionnary"""
    with open(filename, "rt") as f:
        rows = csv.reader(f)
        header = next(rows)
        records = []
        for row in rows:
            if not row:
                continue
            records.append(dict(zip(header, row)))
        return records
