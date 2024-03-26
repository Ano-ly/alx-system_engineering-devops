#!/usr/bin/python3
"""Fetch data via a RestAPI"""
import requests

my_url_todo = 'https://jsonplaceholder.typicode.com/todos'
my_url_user = 'https://jsonplaceholder.typicode.com/users'

todo_data = requests.get(my_url_todo).json()
user_data = requests.get(my_url_user).json()

print(todo_data, user_data)
