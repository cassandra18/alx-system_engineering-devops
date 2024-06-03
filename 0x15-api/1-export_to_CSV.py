#!/usr/bin/python3
"""
Python script to save data in CSV format.
"""
import csv
import requests
import sys


if __name__ == "__main__":
    todos_api_response = requests.get('https://jsonplaceholder.typicode.com/todos/')
    todos_list = todos_api_response.json()

    users_api_response = requests.get('https://jsonplaceholder.typicode.com/users')
    users_list = users_api_response.json()

    for user in users_list:
        if user['id'] == int(sys.argv[1]):
            user_name = user['username']

    with open(sys.argv[1] + '.csv', 'w', newline='') as output_csv:
        csv_output_writer = csv.writer(output_csv, quoting=csv.QUOTE_ALL)

        for todo in todos_list:
            if todo['userId'] == int(sys.argv[1]):
                data_row = [
                    todo['userId'],
                    user_name,
                    todo['completed'],
                    todo['title']
                ]
                csv_output_writer.writerow(data_row)
