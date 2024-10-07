# fileparse.py
#
# Exercise 3.3
import csv


def parse_csv(filename, select=None):
    """reads csv file into a dictionnary"""
    with open(filename, "rt") as f:
        rows = csv.reader(f)
        header = next(rows)
        if select and isinstance(select, (tuple, list)):
            select_indexes = [
                header.index(column) for column in select if column in header
            ]
        else:
            select_indexes = []
        records = []
        for row in rows:
            if not row:
                continue
            selected_columns = [row[index] for index in select_indexes]
            records.append(dict(zip(select, selected_columns)))
        return records
