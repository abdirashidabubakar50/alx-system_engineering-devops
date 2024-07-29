#!/usr/bin/python3
"""This is a python script that uses REST API to fetch the TODO list
progress of all employees and export data in JSON format."""
import json
import urllib.error
import urllib.request



def get_all_employees_todo_json():
    """
    Fetch and export the TODO list progress for all employees to JSON.

    Returns:
        None
    """
    base_url = "https://jsonplaceholder.typicode.com/"

    # Get all users information
    try:
        with urllib.request.urlopen(f"{base_url}users") as response:
            users_data = response.read()
            employees = json.loads(users_data)
    except urllib.error.URLError as e:
        print(f"Error: Unable to fetch data. {e.reason}")
        return
    except json.JSONDecodeError:
        print("Error: Unable to parse employee data.")
        return

    all_tasks = {}

    for employee in employees:
        e_id = employee.get('id')
        employee_name = employee.get('username', 'Unknown')

        # Get TODO list for the employee
        try:
            with urllib.request.urlopen(f"{base_url}todos?userId={e_id}") as response:
                todos_data = response.read()
                todos = json.loads(todos_data)
        except urllib.error.URLError as e:
            print(f"Error: Unable to fetch data for employee {e_id}. {e.reason}")
            continue
        except json.JSONDecodeError:
            print(f"Error: Unable to parse TODO list data for employee {e_id}.")
            continue

        tasks = [{"username": employee_name,
                  "task": task.get('title', 'No title'),
                  "completed": task.get('completed')} for task in todos]

        all_tasks[str(e_id)] = tasks

    # Export to JSON
    json_filename = "todo_all_employees.json"
    with open(json_filename, mode='w') as file:
        json.dump(all_tasks, file)


if __name__ == "__main__":
    """
    Main entry point of the script.
    """
    get_all_employees_todo_json()
