#!/usr/bin/python3
import csv
import json
import requests
from sys import argv

headers = {
    'Accept': 'application/json',
    'Content-Type': 'application/json'
}
csvheader = ["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"]

if __name__ == "__main__":
    """ Functions for gathering  data from an API """
    request_employee = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}/'.format(argv[1]))
    employee = json.loads(request_employee.text)
    employee_name = employee.get("name")
    userName = employee.get("username")
    request_todos = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}/todos'.format(argv[1]))
    tasks = []
    employee_todos = json.loads(request_todos.text)
    
    USER_ID = argv[1]
    
    for dictionary in employee_todos:
        tasks.append([dictionary.get("userId"), userName, dictionary.get("completed"), dictionary.get("title")])
          
with open(f'{USER_ID}.csv', 'w', encoding="UTF8", newline='') as user:
    writer = csv.writer(user)

    writer.writerow(csvheader)
    writer.writerows(tasks)

