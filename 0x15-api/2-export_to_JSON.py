#!/usr/bin/python3
"""
Using what you did in the task #0, extend your Python script to export data
in the JSON format.
Requirements:
    - Records all tasks that are owned by this employee
    - Format must be:
      { "USER_ID": [{"task": "TASK_TITLE", "completed":
      TASK_COMPLETED_STATUS, "username": "USERNAME"}, {"task": "TASK_TITLE",
      "completed": TASK_COMPLETED_STATUS, "username": "USERNAME"}, ... ]}
    - File name must be: USER_ID.json
"""
import json
import requests
import sys

if __name__ == "__main__":
    uid = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com"

    user_url = f"{url}/users/{uid}"
    user_resp = requests.get(user_url)
    user_json = user_resp.json()
    todo_url = f"{url}/todos?userId={uid}"
    todo_resp = requests.get(todo_url)
    todo_json = todo_resp.json()

    filename = f"{uid}.json"

    tasks_list = []
    for task in todo_json:
        task_dict = {}

        task_dict["task"] = task.get("title")
        task_dict["completed"] = task.get("completed")
        task_dict["username"] = user_json.get("username")

        tasks_list.append(task_dict)

    to_json = {uid: tasks_list}

    with open(filename, "w") as file:
        json.dump(to_json, file)
