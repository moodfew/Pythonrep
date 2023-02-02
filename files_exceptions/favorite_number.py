import json

filename = 'number.json'

number = input("What is your favorite number? ")
number = int(number)

with open(filename, 'w') as f:
    json.dump(number, f)
