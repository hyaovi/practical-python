# fileparse.py
#
# Exercise 3.12
import csv


def parse_csv(
    lines,
    select=None,
    types=None,
    has_headers=True,
    delimiter=",",
    silence_errors=True,
):
    """reads csv file into a dictionnary"""
    if type(lines) is str:
        raise SystemExit("requires iterables not filepath:  %s" % lines)
    if select and not has_headers:
        raise RuntimeError("select require  headers")
    rows = csv.reader(lines, delimiter=delimiter)
    records = []
    headers = []
    if has_headers:
        headers = next(rows)
    if select:
        indexes = [headers.index(column) for column in select]
        headers = select
    for line, row in enumerate(rows, start=1):
        try:
            if not row:
                continue
            if select:
                row = [row[index] for index in indexes]

            if types:
                row = [func(val) for func, val in zip(types, row)]

            if headers:
                record = dict(zip(headers, row))
            else:
                record = tuple(row)
        except ValueError as e:
            if not silence_errors:
                print(f"Row: {line} {e}")

        records.append(record)
    return records
