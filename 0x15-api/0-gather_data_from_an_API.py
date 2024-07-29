#!/usr/bin/python3
"""This is a python script that uses REST API for a given employee ID,
returns information about his/her TODO list progress."""
import urllib.request
import json
import sys


def get_employee_todo_progress(e_id):
    """
    Fetch and display the TODO list progress for a given employee ID.

    Args:
        employee_id (int): The ID of the employee.

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

    employee_name = employee.get('name')

    # Get TODO list for the employee
    todos_url = f"{base_url}todos?userId={e_id}"
    with urllib.request.urlopen(todos_url) as response:
        todos_data = response.read()
        todos = json.loads(todos_data)

    # Calculate the number of completed and total tasks
    completed_tasks = [todo for todo in todos if todo.get('completed')]
    total_tasks = len(todos)
    number_of_done_tasks = len(completed_tasks)

    # Display the progress
    print(f"Employee {employee_name} is done with tasks({number_of_done_tasks}/"
          f"{total_tasks}):")
    for task in completed_tasks:
        print(f"\t {task.get('title')}")


if __name__ == "__main__":
    """
    Main entry point of the script. Validates the input and calls the function
    to get and display the TODO list progress.
    """
    if len(sys.argv) != 2:
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Error: Employee ID must be an integer.")
        sys.exit(1)

    get_employee_todo_progress(employee_id)
