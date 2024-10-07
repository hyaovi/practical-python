# fileparse.py
#
# Exercise 3.5 type conversion
import csv


def parse_csv(filename, select=None, types=None):
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
            # if types:
            #     selected_columns = [
            #         types[index](selected_columns[index])
            #         for index in range(0, len(types))
            #     ]
            if types:
                selected_columns = [
                    func(val) for func, val in zip(types, selected_columns)
                ]
            records.append(dict(zip(select, selected_columns)))
        return records
