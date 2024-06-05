#!/usr/bin/python3

"""
Python script to save data in JSON format.
"""

import json
import requests
import sys

if __name__ == "__main__":
    api_response_todos = requests.get(
            'https://jsonplaceholder.typicode.com/todos/')
    todos_list = api_response_todos.json()

    user_details = []
    api_response_users = requests.get('https://jsonplaceholder.typicode.com/users')
    users_list = api_response_users.json()

    for user in users_list:
        if user['id'] == int(sys.argv[1]):
            user_name = user['username']
            user_id = user['id']

    user_task_list = []

    for todo in todos_list:
        task_info = {}

        if todo['userId'] == int(sys.argv[1]):
            task_info['task'] = todo['title']
            task_info['completed'] = todo['completed']
            task_info['username'] = user_name
            user_task_list.append(task_info)

    user_data = {}
    user_data[user_id] = user_task_list
    json_data = json.dumps(user_data)

    with open(sys.argv[1] + ".json", "w") as json_file:
        json_file.write(json_data)
