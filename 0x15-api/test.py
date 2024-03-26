#!/usr/bin/python3
import json

str_list = ["rrrr", " us"]
with open("file.json", "w") as filee:
    for item in str_list:
    	json.dump(item, filee)
