#!/usr/bin/python3
import json
import requests
from sys import argv

# Check if the script is executed as the main program
if __name__ == "__main__":
    """ Functions for gathering data from an API """

    # Send a GET request to retrieve user data based on the provided user ID
    request_employee = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}/'.format(argv[1]))

    # Parse the JSON response into a Python dictionary
    employee = json.loads(request_employee.text)

    # Extract relevant user information
    employee_name = employee.get("name")
    USERNAME = employee.get("username")

    # Send a GET request to retrieve the user's TODO list
    request_todos = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}/todos'.format(argv[1]))

    # Initialize an empty list to store task data
    tasks = []

    # Parse the JSON response into a Python list
    employee_todos = json.loads(request_todos.text)

    # Iterate through each TODO item
    for dictionary in employee_todos:
        USER_ID = dictionary.get("userId")
        TASK_TITLE = dictionary.get("title")
        TASK_COMPLETED_STATUS = dictionary.get("completed")

        # Construct a dictionary for each task containing task title, completion status, and username
        task_data = {
            "task": TASK_TITLE,
            "completed": TASK_COMPLETED_STATUS,
            "username": USERNAME
        }

        # Append the task data to the list of tasks
        tasks.append(task_data)

    # Create a dictionary with user ID and the list of tasks
    result = {
        "USER_ID": USER_ID,
        "tasks": tasks
    }

    # Print the result as a nicely formatted JSON string
    print(json.dumps(result, indent=2))
