#!/usr/bin/python3
import csv
import json
import requests
from sys import argv

""" Define HTTP headers for the API requests"""
headers = {
    'Accept': 'application/json',
    'Content-Type': 'application/json'
}

"""Define the header for the CSV file"""
csvheader = ["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"]

if __name__ == "__main__":
    """Get the user ID from the command-line argument"""
    user_id = argv[1]
    """ Step 1: Retrieve user information from the JSONPlaceholder API using the provided user ID."""
    request_employee = requests.get(
        f'https://jsonplaceholder.typicode.com/users/{user_id}')
    employee = json.loads(request_employee.text)
    employee_name = employee.get("name")
    userName = employee.get("username")

    """ Step 2: Retrieve the user's tasks from the API."""
    request_todos = requests.get(
        f'https://jsonplaceholder.typicode.com/users/{user_id}/todos')
    tasks = []
    employee_todos = json.loads(request_todos.text)

    """ Step 3: Create a list of tasks including user ID, username, task completion status, and task title."""
    for dictionary in employee_todos:
        tasks.append([dictionary.get("userId"), userName, dictionary.get("completed"), dictionary.get("title")])

    """ Step 4: Generate the CSV filename based on the user's ID."""
    USER_ID = user_id

    """Step 5: Create and write the data to a CSV file with the generated filename."""
    with open(f'{USER_ID}.csv', 'w', encoding="UTF8", newline='') as user:
        writer = csv.writer(user)
        writer.writerow(csvheader)
        writer.writerows(tasks)

