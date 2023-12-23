#!/usr/bin/python3
import urllib
import requests
import sys

if len(sys.argv) > 1:
    EMPLOYEE_ID = sys.argv[1]
else:
    exit

URL = 'https://jsonplaceholder.typicode.com'
EMPLOYEE = requests.get(f'{URL}/users/{EMPLOYEE_ID}').json()
TOTAL_TASKS = requests.get(f'{URL}/todos?userId={EMPLOYEE_ID}').json()
DONE_TASKS = requests.get(
    f'{URL}/todos?userId={EMPLOYEE_ID}&completed=true').json()
NUMBER_OF_TOTAL_TASKS = len(TOTAL_TASKS)
NUMBER_OF_DONE_TASKS = len(DONE_TASKS)

print(f'Employee {EMPLOYEE["name"]} is done with tasks' +
      f'({NUMBER_OF_DONE_TASKS}/{NUMBER_OF_TOTAL_TASKS}):')
for i in DONE_TASKS:
    print(f'\t{i["title"]}')
