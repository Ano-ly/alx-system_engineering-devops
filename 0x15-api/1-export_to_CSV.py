#!/usr/bin/python3
"""
Fetch data via a RestAPI, jsonplaceholder and write
to csv file
"""

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
    str_lists = []
    with open ("USER_ID.csv", "w") as csvfile:
        csv_obj = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for task in tasks:
            if task.get("completed"):
                status = "True"
            else:
                status = "False"
            title = task.get("title")
            str_list = [sys.argv[1], username, status, title]
            str_lists.append(str_list)
        csv_obj.writerows(str_lists)
