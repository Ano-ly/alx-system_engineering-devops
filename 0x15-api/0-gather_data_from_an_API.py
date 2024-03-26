#!/usr/bin/python3
"""Fetch data via a RestAPI"""
import requests

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
for dic in todo_dic:
    if dic_get("user.Id") == sys.argv[1]:
        tasks.append(dic)
for tasks in task:
    if task.get("completed"):
        done_titles.append(task.get("title"))

top_str = "Employee {} is done with tasks ({}/{}):"
content = "\n\t ".join(done_titles)

print(top_str)
print("\t ".end="")
print(content)
