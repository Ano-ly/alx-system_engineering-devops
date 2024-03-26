#!/usr/bin/python3
"""Fetch data via a RestAPI"""

if __name__ == "__main__":
    import requests
    import sys

    my_url_todo = 'https://jsonplaceholder.typicode.com/todos'
    my_url_user = 'https://jsonplaceholder.typicode.com/users'

    todo_data = requests.get(my_url_todo).json()
    user_data = requests.get(my_url_user).json()

    done_titles = []
    tasks = []
    name = ""

    for dic in user_data:
        if str(dic.get("id")) == sys.argv[1]:
            name = dic.get("name")
    for dic in todo_data:
        if str(dic.get("userId")) == sys.argv[1]:
            tasks.append(dic)
    for task in tasks:
        if task.get("completed"):
            done_titles.append(task.get("title"))

    top_str = "Employee {} is done with tasks({}/{}):"\
              .format(name, len(done_titles), len(tasks))
    content = "\n\t ".join(done_titles)

    print(top_str)
    print("\t ", end="")

    print(content)
