#!/usr/bin/python3
"""_summary_
"""
import json
import requests
import sys
import urllib


def getUserTasks(EMPLOYEE_ID):
    """_summary_

    Args:
        EMPLOYEE_ID (_type_): _description_
    """
    URL = 'https://jsonplaceholder.typicode.com'
    EMPLOYEE = requests.get(f'{URL}/users/{EMPLOYEE_ID}').json()
    TOTAL_TASKS = requests.get(f'{URL}/todos?userId={EMPLOYEE_ID}').json()
    USERNAME = EMPLOYEE['username']

    tasks = []

    for i in TOTAL_TASKS:
        tasks.append({"task": i["title"],
                      "completed": i["completed"],
                      "username": USERNAME})

    user = {EMPLOYEE_ID: tasks}
    with open(f"{EMPLOYEE_ID}.json", "w") as outfile:
        outfile.write(json.dumps(user))


if __name__ == "__main__":
    """_summary_
    """
    if len(sys.argv) > 1:
        getUserTasks(sys.argv[1])
    else:
        exit
