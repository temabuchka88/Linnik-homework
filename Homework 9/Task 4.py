import csv
import json

with open('Homework 9\\task_3_file.json', 'r') as file:
    json_reader = json.load(file)
filds = ['id', 'name', 'age', 'phone_number']

with open('Homework 9\\task_3_file.csv', 'w', newline='') as csv_file:
    writer = csv.DictWriter(csv_file,fieldnames=filds)
    writer.writeheader()
    for key, value in json_reader.items():
        writer.writerow({'id':key, 'name': value[0], 'age': value[1], 'phone_number' : ''})