#!/usr/bin/python3

import json
import requests

def fetch_all_employees_data():
    """Fetch and record tasks for all employees from a REST API."""
    
    # Endpoints
    users_url = "https://jsonplaceholder.typicode.com/users"
    todos_url = "https://jsonplaceholder.typicode.com/todos"
    
    # Fetch all users
    users_response = requests.get(users_url)
    users = users_response.json()
    
    # Fetch all todos
    todos_response = requests.get(todos_url)
    todos = todos_response.json()

    # Create a dictionary to hold data for all employees
    all_employees_data = {}

    # Iterate over each user and fetch their tasks
    for user in users:
        user_id = user.get('id')
        username = user.get('username')
        
        user_tasks = [
            {
                "username": username,
                "task": todo.get('title'),
                "completed": todo.get('completed')
            }
            for todo in todos if todo.get('userId') == user_id
        ]
        
        all_employees_data[str(user_id)] = user_tasks

    # Export the data to a JSON file
    with open("todo_all_employees.json", 'w') as json_file:
        json.dump(all_employees_data, json_file, indent=4)

    print(f"Data exported to todo_all_employees.json")

if __name__ == "__main__":
    fetch_all_employees_data()
