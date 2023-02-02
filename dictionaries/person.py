# Make an empty list to store people
people = []


# Define some people and add them to the list
person = {'first_name': 'Alex',
            'last_name': 'Smith',
            'age': '16',
            'city': 'Tirane',
            }
people.append(person)


person = {'first_name': 'Denis',
            'last_name': 'Rr',
            'age': '16',
            'city': 'Tirane',
            }
people.append(person)


# Display all the information for each user
for person in people:
    print(f"First name: {person['first_name']}")
    print(f"Last name: {person['last_name']}")
    print(f"Age: {person['age']}")
    print(f"City: {person['city']}\n")

