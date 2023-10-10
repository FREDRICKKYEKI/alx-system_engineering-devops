#!/usr/bin/python3
"""
Using what you did in the task #0, extend your Python script to export data in
the JSON format.
Requirements:
    - Records all tasks from all employees
    - Format must be: { "USER_ID": [ {"username": "USERNAME",
      "task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS},
      {"username": "USERNAME", "task": "TASK_TITLE",
      "completed": TASK_COMPLETED_STATUS}, ... ],
      "USER_ID": [ {"username": "USERNAME",
      "task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS},
      {"username": "USERNAME", "task": "TASK_TITLE",
      "completed": TASK_COMPLETED_STATUS}, ... ]}
    - File name must be: todo_all_employees.json
"""
import json
import requests
import sys

if __name__ == "__main__":

    todos_url = "https://jsonplaceholder.typicode.com/todos"
    users_url = "https://jsonplaceholder.typicode.com/users"

    todos_resp = requests.get(todos_url)
    users_resp = requests.get(users_url)

    todos_json = todos_resp.json()
    users_json = users_resp.json()

    filename = "todo_all_employees.json"

    user_dict = {}
    for user in users_json:
        tasks_list = []
        for todo in todos_json:
            if todo.get('userId') == user.get('id'):
                task_dict = {}
                task_dict["username"] = user.get("username")
                task_dict["task"] = todo.get("title")
                task_dict["completed"] = todo.get("completed")
                tasks_list.append(task_dict)

        user_dict[user.get('id')] = tasks_list

    with open(filename, "w") as file:
        json.dump(user_dict, file)
