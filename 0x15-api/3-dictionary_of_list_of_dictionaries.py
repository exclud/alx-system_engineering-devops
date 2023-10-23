#!/usr/bin/python3
"""Export TODO list progress of all employees to JSON"""

import json
import requests


def get_all_employees_todo_progress():
    """Export the TODO list progress for all employees."""

    # Endpoints
    users_url = "https://jsonplaceholder.typicode.com/users"
    todos_url = "https://jsonplaceholder.typicode.com/todos"

    # Fetch all employees details
    users_response = requests.get(users_url)
    users_data = users_response.json()

    # Fetch all todos
    todos_response = requests.get(todos_url)
    todos_data = todos_response.json()

    user_tasks = {}
    for user in users_data:
        user_tasks[str(user['id'])] = []

    for task in todos_data:
        task_dict = {
            "username": task["userId"],
            "task": task["title"],
            "completed": task["completed"]
        }
        user_tasks[str(task["userId"])].append(task_dict)

    with open("todo_all_employees.json", 'w') as json_file:
        json.dump(user_tasks, json_file, indent=4)


if __name__ == "__main__":
    get_all_employees_todo_progress()
