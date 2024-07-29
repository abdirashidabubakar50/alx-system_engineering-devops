#!/usr/bin/python3
"""This is a python script that uses REST API for a given employee ID,
returns information about his/her TODO list progress and exports data in
CSV format."""
import csv
import json
import sys
import urllib.request
import urllib.error


def get_employee_todo_csv(e_id):
    """
    Fetch and display the TODO list progress for a given employee ID and
    export to CSV.

    Args:
        e_id (int): The ID of the employee.

    Returns:
        None
    """
    base_url = "https://jsonplaceholder.typicode.com/"

    # Get employee information
    try:
        with urllib.request.urlopen(f"{base_url}users/{e_id}") as response:
            user_data = response.read()
            employee = json.loads(user_data)
    except urllib.error.HTTPError as e:
        if e.code == 404:
            print(f"Error: User with ID {e_id} not found.")
            return
        else:
            raise
    except urllib.error.URLError as e:
        print(f"Error: Unable to fetch data. {e.reason}")
        return
    except json.JSONDecodeError:
        print("Error: Unable to parse employee data.")
        return

    employee_name = employee.get('username', 'Unknown')

    # Get TODO list for the employee
    try:
        with urllib.request.urlopen(f"{base_url}todos?userId={e_id}") as response:
            todos_data = response.read()
            todos = json.loads(todos_data)
    except urllib.error.URLError as e:
        print(f"Error: Unable to fetch data. {e.reason}")
        return
    except json.JSONDecodeError:
        print("Error: Unable to parse TODO list data.")
        return

    # Export to CSV
    csv_filename = f"{e_id}.csv"
    with open(csv_filename, mode='w', newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        for task in todos:
            writer.writerow([e_id, employee_name, task.get('completed'),
                             task.get('title', 'No title')])


if __name__ == "__main__":
    """
    Main entry point of the script. Validates the input and calls the function
    to get and display the TODO list progress and export to CSV.
    """
    if len(sys.argv) != 2:
        print("Usage: python3 1-export_to_CSV.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Error: Employee ID must be an integer.")
        sys.exit(1)

    get_employee_todo_csv(employee_id)
