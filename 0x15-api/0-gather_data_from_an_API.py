#!/usr/bin/python3
"""
Write a Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
Requirements:
    - You must use urllib or requests module
    - The script must accept an integer as a parameter, which is the employee
      ID
    - The script must display on the standard output the employee TODO list
      progress in this exact format:
        - First line: Employee EMPLOYEE_NAME is done with tasks
          (NUMBER_OF_DONE_TASKS/TOTAL_NUMBER_OF_TASKS):
            - EMPLOYEE_NAME: name of the employee
            - NUMBER_OF_DONE_TASKS: number of completed tasks
            - TOTAL_NUMBER_OF_TASKS: total number of tasks, which is the sum
              of completed and non-completed tasks
    - Second and N next lines display the title of completed tasks: TASK_TITLE
      (with 1 tabulation and 1 space before the TASK_TITLE)
"""
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
    completed_tasks = []

    for task in todo_json:
        if task.get("completed"):
            completed_tasks.append(task)

    NUMBER_OF_DONE_TASKS = len(completed_tasks)
    TOTAL_NUMBER_OF_TASKS = len(todo_json)
    EMPLOYEE_NAME = user_json.get('name')

    result = f"Employee {EMPLOYEE_NAME} is done with tasks"\
             f"({NUMBER_OF_DONE_TASKS}/{TOTAL_NUMBER_OF_TASKS}):"

    print(result)
    for task in completed_tasks:
        print("\t", task.get("title"))
