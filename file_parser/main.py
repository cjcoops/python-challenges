import csv
import tabulate
import argparse
from datetime import datetime
from collections import Counter


class EmployeeDataParser:
    def __init__(self, file_path):
        self.file_path = file_path
        self.employees = self.load_data()

    def load_data(self):
        employees = []
        with open(self.file_path, mode="r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                row["salary"] = int(row["salary"])
                row["start_date"] = datetime.strptime(row["start_date"], "%Y-%m-%d")
                employees.append(row)
        return employees

    def filter_by_column(self, column, value):
        return [emp for emp in self.employees if str(emp[column]) == value]

    def filter_by_department(self, department):
        return [
            employee
            for employee in self.employees
            if employee["department"].lower() == department.lower()
        ]

    def filter_by_date_range(self, start_date, end_date):
        return [
            employee
            for employee in self.employees
            if start_date <= employee["start_date"] <= end_date
        ]

    def filter_by_salary(self, min=None, max=None):
        results = self.employees

        if min is not None:
            results = [employee for employee in results if min <= employee["salary"]]

        if max is not None:
            results = [employee for employee in results if employee["salary"] <= max]

        return results

    def get_department_count(self):
        departments = [employee["department"] for employee in self.employees]
        departments_count = Counter(departments)
        return departments_count

    def sort_by(self, key):
        return sorted(self.employees, key=lambda e: e[key])

    def print(self, employees):
        print(tabulate.tabulate(employees))

    def write_to_csv(self, data, filename):
        with open(filename, mode="w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=data[0].keys())
            writer.writeheader()
            writer.writerows(data)

        print(f"Data written to {filename}")


def parse_query(query):
    """Parse a simple query in the form 'column=value'."""
    try:
        column, value = query.split("=")
        return column.strip(), value.strip()
    except ValueError:
        raise ValueError("Query must be in the format 'column=value'")


def main():
    cli = argparse.ArgumentParser(
        prog="Employee Data Parser", description="Parses a CSV of employee data"
    )

    cli.add_argument(
        "--file",
        type=str,
        required=True,
        help="Path to the CSV file containing employee data.",
    )
    cli.add_argument(
        "--query",
        type=str,
        required=False,
        help='Query in the form "column=value" (e.g., department=Engineering).',
    )

    args = cli.parse_args()

    parser_instance = EmployeeDataParser(args.file)

    if args.query:
        try:
            column, value = parse_query(args.query)
            filtered_employees = parser_instance.filter_by_column(column, value)
            if filtered_employees:
                parser_instance.print(filtered_employees)
            else:
                print("No matching employees found for the given query.")
        except ValueError as e:
            print(e)
    else:
        parser_instance.print(parser_instance.employees)


if __name__ == "__main__":
    main()

# parser.print(parser.filter_by_department("marketing"))
# parser.print(parser.filter_by_date_range(datetime(2023, 8, 1), datetime.now()))
# parser.print(parser.filter_by_salary(max=90000))
# print(parser.get_department_count())
# parser.print(parser.sort_by("last_name"))
# employees_by_last_name = parser.sort_by("last_name")
# parser.write_to_csv(employees_by_last_name, "file_parser/output.csv")
