pets = []

pet = {'type': 'python',
       'weight': 43,
       'owner': 'alex',
       'age': 13,
       'name': 'bobi'}
pets.append(pet)

pet = {'type': 'cat',
       'weight': 17,
       'owner': 'denis',
       'age': 5,
       'name': 'qamile'}
pets.append(pet)

pet= {'type': 'dawg',
      'weight': 25,
      'owner': 'alvi',
      'age': 5,
      'name': 'frenkli'}

pets.append(pet)

for pet in pets:
    print(f"\nHere's what I know about {pet['name'].title()}")
    for key, value in pet.items():
        print(f"{key.title()}: {value}")
