#!/usr/bin/python3
"""
Using what you did in the task #0, extend your Python script to export data
in the CSV format.
Requirements:
    - Records all tasks that are owned by this employee
    - Format must be: "USER_ID","USERNAME","TASK_COMPLETED_STATUS",
      "TASK_TITLE"
    - File name must be: USER_ID.csv
"""
import csv
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

    filename = f"{uid}.csv"
    with open(filename, "w") as f:
        csv_writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        for todo in todo_json:

            USER_ID = f"{uid}"
            USERNAME = f"{user_json.get('username')}"
            TASK_COMPLETED_STATUS = f"{todo.get('completed')}"
            TASK_TITLE = f"{todo.get('title')}"

            csv_writer.writerow([USER_ID, USERNAME, TASK_COMPLETED_STATUS,
                                 TASK_TITLE])
