#!/usr/bin/python3

""""Fetch and Record Todo List"""


import csv
import requests
import sys


def get_employee_todo_progress(employee_id):
    """Fetch and record the TODO list progress
    for a given employee ID from a REST API."""

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

    # Filter completed tasks
    done_tasks = [task for task in todos_data if task.get('completed')]

    # Print the employee TODO list progress to the console
    print(f"Employee {user_data.get('name')} is done with tasks({len(done_tasks)}/{len(todos_data)}):")
    for task in done_tasks:
        print("\t " + task.get('title'))

    # Write all tasks to a CSV file
    with open(f"{employee_id}.csv", mode='w', newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_MINIMAL)
        writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])

        for task in todos_data:
            writer.writerow([employee_id, user_data.get('username'), task.get('completed'), task.get('title')])

    print(f"Data exported to {employee_id}.csv")


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
