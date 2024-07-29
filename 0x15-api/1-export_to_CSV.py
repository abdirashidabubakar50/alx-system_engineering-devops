#!/usr/bin/python3
"""This is a python script that uses REST API for a given employee ID,
returns information about his/her TODO list progress."""
import csv
import sys

get_employee_todo = __import__('0-gather_data_from_an_API').get_employee_todo


def export_to_csv(employee_id):
    """
    Export TODO list data for a given employee ID to a CSV file.

    Args:
        employee_id (int): The ID of the employee.

    Returns:
        None
    """
    data = get_employee_todo(employee_id)
    if data is None:
        return

    employee = data['employee']
    todos = data['todos']

    csv_filename = f"{employee_id}.csv"
    with open(csv_filename, mode='w', newline='') as csv_file:
        writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
        for todo in todos:
            writer.writerow([employee_id, employee.get('username'),
                             todo.get('completed'), todo.get('title')])


if __name__ == "__main__":
    """
    Main entry point of the script. Validates the input and calls the function
    to export the TODO list data to a CSV file.
    """
    if len(sys.argv) != 2:
        print("Usage: python3 1-export_to_CSV.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Error: Employee ID must be an integer.")
        sys.exit(1)

    export_to_csv(employee_id)
