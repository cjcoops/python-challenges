import csv
import tabulate
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


parser = EmployeeDataParser("file_parser/employee_data_large.csv")
# parser.print(parser.filter_by_department("marketing"))
# parser.print(parser.filter_by_date_range(datetime(2023, 8, 1), datetime.now()))
# parser.print(parser.filter_by_salary(max=90000))
# print(parser.get_department_count())
# parser.print(parser.sort_by("last_name"))
employees_by_last_name = parser.sort_by("last_name")
parser.write_to_csv(employees_by_last_name, "file_parser/output.csv")
