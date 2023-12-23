#!/usr/bin/python3
"""_summary_
"""
import json
import requests
import sys
import urllib


URL = 'https://jsonplaceholder.typicode.com'


def getUserTasks(EMPLOYEE_ID):
    """_summary_

    Args:
        EMPLOYEE_ID (_type_): _description_
    """
    EMPLOYEE = requests.get(f'{URL}/users/{EMPLOYEE_ID}').json()
    TOTAL_TASKS = requests.get(f'{URL}/todos?userId={EMPLOYEE_ID}').json()
    USERNAME = EMPLOYEE['username']

    tasks = []

    for i in TOTAL_TASKS:
        tasks.append({"username": USERNAME,
                      "task": i["title"],
                      "completed": i["completed"]})

    return tasks


def getAllUsers():
    ALL_USERS = requests.get(f'{URL}/users').json()
    user_obj = {}
    for user in ALL_USERS:
        user_obj[user["id"]] = getUserTasks(user["id"])

    with open("todo_all_employees.json", "w") as outfile:
        outfile.write(json.dumps(user_obj))


if __name__ == "__main__":
    """_summary_
    """
    getAllUsers()
