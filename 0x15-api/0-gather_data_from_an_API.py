#!/usr/bin/python3
"""
 Python script that, using this REST API, for a given employee ID.
 Returns information about his/her TODO list progress.
"""
import requests
import sys


if __name__ == "__main__":
    responseTodos = requests.get('https://jsonplaceholder.typicode.com/todos/')
    data_todos = responseTodos.json()
    completed_tasks = 0
    total_tasks = 0
    task_list = []
    response_users = requests.get('https://jsonplaceholder.typicode.com/users')
    data_users = response_users.json()

    for user_entry in data_users:
        if user_entry.get('id') == int(sys.argv[1]):
            employee_name = user_entry.get('name')

    for todo_entry in data_todos:
        if todo_entry.get('userId') == int(sys.argv[1]):
            total_tasks += 1

            if todo_entry.get('completed') is True:
                completed_tasks += 1
                task_list.append(todo_entry.get('title'))

    print("Employee {} is done with tasks({}/{}):".format(employee_name,
                                                          completed_tasks,
                                                          total_tasks))

    for task_item in task_list:
        print("\t {}".format(task_item))
