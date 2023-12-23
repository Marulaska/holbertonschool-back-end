#!/usr/bin/python3
"""_summary_
"""
import requests
import sys
import urllib
import csv


def getUserTasks(EMPLOYEE_ID):
    """_summary_

    Args:
        EMPLOYEE_ID (_type_): _description_
    """
    URL = 'https://jsonplaceholder.typicode.com'
    TOTAL_TASKS = requests.get(f'{URL}/todos?userId={EMPLOYEE_ID}').json()
    EMPLOYEE = requests.get(f'{URL}/users/{EMPLOYEE_ID}').json()
    USERNAME = EMPLOYEE['username']

    f = csv.writer(open(f"{EMPLOYEE_ID}.csv", "w", newline=''), quoting=csv.QUOTE_ALL)
    # f.writer(open(f"{EMPLOYEE_ID}.csv", 'w', encoding='utf8'))

    for i in TOTAL_TASKS:
        f.writerow([i['userId'],
                   USERNAME,
                   i['completed'],
                   i['title']])


if __name__ == "__main__":
    """_summary_
    """
    if len(sys.argv) > 1:
        getUserTasks(sys.argv[1])
    else:
        exit
