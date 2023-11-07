import csv
import json

# with open('db/db.csv', 'r', newline='') as csv_file:
#     lines = csv.reader(csv_file, delimiter=',')
#     for line in lines:
#         print(line, type(line))


def get_users():
    with open('db/db.json', 'r') as json_file:
        db = json.load(json_file)
    return db['db']
