#!/usr/bin/python3
"""This is a python script that uses REST API for a given employee ID,
returns information about his/her TODO list progress and exports data in
JSON format."""
import json
import sys
import urllib.request
import urllib.error


def get_employee_todo_json(e_id):
    """
    Fetch and display the TODO list progress for a given employee ID and
    export to JSON.

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

    # Create the JSON structure
    tasks = [{"task": task.get('title', 'No title'),
              "completed": task.get('completed'),
              "username": employee_name} for task in todos]

    json_data = {str(e_id): tasks}

    # Export to JSON
    json_filename = f"{e_id}.json"
    with open(json_filename, mode='w') as file:
        json.dump(json_data, file)


if __name__ == "__main__":
    """
    Main entry point of the script. Validates the input and calls the function
    to get and display the TODO list progress and export to JSON.
    """
    if len(sys.argv) != 2:
        print("Usage: python3 2-export_to_JSON.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Error: Employee ID must be an integer.")
        sys.exit(1)

    get_employee_todo_json(employee_id)
