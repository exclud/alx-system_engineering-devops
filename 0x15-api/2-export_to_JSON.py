#!/usr/bin/python3
"""Fetch and Record todo list files"""

import json
import requests
import sys


def get_employee_todo_progress(employee_id):
    """Fetch and record the TODO list progress for a given employee ID."""
    # Endpoints
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    todos_url = (
        f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"
    )

    # Fetch employee details
    user_response = requests.get(user_url)
    user_data = user_response.json()

    # Fetch todos for the employee
    todos_response = requests.get(todos_url)
    todos_data = todos_response.json()

    # Filter completed tasks for console output
    done_tasks = [task for task in todos_data if task.get('completed')]

    # Print the employee TODO list progress to the console
    print(f"Employee {user_data.get('name')} is done with "
          f"tasks({len(done_tasks)}/{len(todos_data)}):")
    for task in done_tasks:
        print("\t " + task.get('title'))

    # Prepare data for JSON export
    tasks_list = [
        {
            "task": task.get('title'),
            "completed": task.get('completed'),
            "username": user_data.get('username')
        }
        for task in todos_data
    ]
    json_data = {str(employee_id): tasks_list}

    # Write all tasks to a JSON file
    with open(f"{employee_id}.json", 'w') as json_file:
        json.dump(json_data, json_file, indent=4)

    print(f"Data exported to {employee_id}.json")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: {} <employee_id>".format(sys.argv[0]))
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Employee ID must be an integer.")
        sys.exit(1)

    get_employee_todo_progress(employee_id)
