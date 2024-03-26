#!/usr/bin/python3
"""Write output to CSV file"""

import csv

date = "ffffff I love"

with open("USER_ID.csv", "w") as csv_file:
    name = csv.writer(csv_file, delimiter=",")
    name.writerow(date)
