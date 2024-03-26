#!/usr/bin/python3
"""
Fetch data via a RestAPI, jsonplaceholder and write
to json file all employees data
"""
import json

if __name__ == "__main__":
    """Don't run script if imported"""
    import requests
    import sys
    import csv

    my_url_todo = 'https://jsonplaceholder.typicode.com/todos'
    my_url_user = 'https://jsonplaceholder.typicode.com/users'

    todo_data = requests.get(my_url_todo).json()
    user_data = requests.get(my_url_user).json()

    super_dict = {}
    for dict in user_data:
        tasks = []
        name = ""
        user_id = dict.get("id")
        name = dict.get("name")
        username = dict.get("username")
        for dict in todo_data:
            if dict.get("userId") == user_id:
                tasks.append(dict)

        inner_list = []
        for task in tasks:
            inner_dict = {}
            inner_dict["task"] = task.get("title")
            inner_dict["completed"] = task.get("completed")
            inner_dict["username"] = username
            inner_list.append(inner_dict)
        outer_dict = {user_id: inner_list}
        super_dict.update(outer_dict)
    with open("todo_all_employees.json", "w") as jfile:
        json.dump(super_dict, jfile)
