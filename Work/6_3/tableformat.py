class FormatError(Exception):
    pass


class TableFormatter:
    def headings(self, headers):
        """Emit the table heading"""
        raise NotImplementedError()

    def row(self, rowdata):
        """Emit a single row of data"""
        raise NotImplementedError()


class TextTableFormater(TableFormatter):
    def headings(self, headers):
        for h in headers:
            print(f"{h:>10s}", end=" ")

        print()
        print(("_" * 10 + " ") * len(headers))

    def row(self, rowdata):
        for data in rowdata:
            print(f"{data:>10s}", end=" ")
        print()


class CSVTableFormatter(TableFormatter):
    """output data in CSV format"""

    def headings(self, headers):
        print(",".join(headers))

    def row(self, rowdata):
        print(",".join(rowdata))


class HTMLTableFormatter(TableFormatter):
    """Output data in html table format"""

    def headings(self, headers):
        print("<tr>", end="")
        for h in headers:
            print(f"<th>{h}</th>", end="")
        print("</tr>")

    def row(self, rowdata):
        print("<tr>", end="")
        for d in rowdata:
            print(f"<td>{d}</td>", end="")
        print("</tr>")


def create_formatter(fmt):
    if fmt == "txt":
        return TextTableFormater()
    elif fmt == "csv":
        return CSVTableFormatter()
    elif fmt == "html":
        return HTMLTableFormatter()
    else:
        raise FormatError(f"unknown format: {fmt}")


def print_table(table_data, columns, formatter: TableFormatter):
    formatter.headings(columns)
    for row in table_data:
        formatter.row([str(getattr(row, colname, "N/A")) for colname in columns])
