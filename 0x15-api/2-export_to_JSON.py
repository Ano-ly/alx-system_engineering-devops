#!/usr/bin/python3
"""
Fetch data via a RestAPI, jsonplaceholder and write
to json file
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

    tasks = []
    name = ""

    for dic in user_data:
        if str(dic.get("id")) == sys.argv[1]:
            name = dic.get("name")
            username = dic.get("username")
    for dic in todo_data:
        if str(dic.get("userId")) == sys.argv[1]:
            tasks.append(dic)

    inner_list = []
    for task in tasks:
        inner_dict = {}
        inner_dict["task"] = task.get("title")
        inner_dict["completed"] = task.get("completed")
        inner_dict["username"] = username
        inner_list.append(inner_dict)
    outer_dic = {str(sys.argv[1]): inner_list}
    with open("{}.json".format(sys.argv[1]), "w") as jfile:
        json.dump(outer_dic, jfile)
