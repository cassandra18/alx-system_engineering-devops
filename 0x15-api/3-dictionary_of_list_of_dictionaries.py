#!/usr/bin/python3
"""
Python script to save data in JSON format
Records all tasks for all employees
"""
import json
import requests


if __name__ == "__main__":
    response_tasks = requests.get(
        'https://jsonplaceholder.typicode.com/todos/')
    tasks_list = response_tasks.json()

    response_users = requests.get('https://jsonplaceholder.typicode.com/users')
    users_list = response_users.json()

    all_users_tasks = {}

    for user in users_list:
        tasks_for_user = []

        for task in tasks_list:
            task_details = {}

            if user['id'] == task['userId']:
                task_details['username'] = user['username']
                task_details['task'] = task['title']
                task_details['completed'] = task['completed']
                tasks_for_user.append(task_details)

        all_users_tasks[user['id']] = tasks_for_user

    with open("todo_all_employees.json", "w") as json_file:
        json_data = json.dumps(all_users_tasks)
        json_file.write(json_data)
