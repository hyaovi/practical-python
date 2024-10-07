# fileparse.py
#
# Exercise 3.5 type conversion
import csv


def parse_csv(filename, select=None, types=None, has_headers=True):
    """reads csv file into a dictionnary"""
    with open(filename, "rt") as f:
        rows = csv.reader(f)
        records = []
        headers = []
        if has_headers:
            headers = next(rows)
        if select:
            indexes = [headers.index(column) for column in select]
            headers = select
        for row in rows:
            if not row:
                continue
            if headers:
                row = [row[index] for index in indexes]

            if types:
                row = [func(val) for func, val in zip(types, row)]

            if headers:
                record = dict(zip(headers, row))
            else:
                record = tuple(row)
            records.append(record)
        return records
