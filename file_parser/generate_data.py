import csv
import random
from faker import Faker
from datetime import date

# Initialize Faker for generating random names, departments, and dates
fake = Faker()

# List of departments and a range for generating salaries
departments = ["Engineering", "Marketing", "HR", "Sales"]
salary_range = (60000, 120000)


# Function to generate employee data
def generate_employee_data(num_rows):
    employees = []
    for i in range(1, num_rows + 1):
        employee = {
            "employee_id": 1000 + i,
            "first_name": fake.first_name(),
            "last_name": fake.last_name(),
            "department": random.choice(departments),
            "salary": random.randint(*salary_range),
            "start_date": fake.date_between(
                start_date=date(2018, 1, 1), end_date=date(2023, 12, 31)
            ),
        }
        employees.append(employee)
    return employees


# Function to write the employee data to a CSV file
def write_employee_csv(filename, num_rows):
    fieldnames = [
        "employee_id",
        "first_name",
        "last_name",
        "department",
        "salary",
        "start_date",
    ]
    employees = generate_employee_data(num_rows)

    with open(filename, mode="w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for employee in employees:
            writer.writerow(
                {
                    "employee_id": employee["employee_id"],
                    "first_name": employee["first_name"],
                    "last_name": employee["last_name"],
                    "department": employee["department"],
                    "salary": employee["salary"],
                    "start_date": employee["start_date"],
                }
            )


# Specify the number of rows and file name
num_rows = 10000  # Change this to generate more/less rows
output_file = "file_parser/employee_data_large.csv"

# Generate the CSV file
write_employee_csv(output_file, num_rows)
print(f"{num_rows} rows of employee data written to {output_file}")
