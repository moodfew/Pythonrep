favorite_numbers = {'denis': [9, 7, 3],
                    'jonis': [27, 7, 17],
                    'kliton': [5, 32, 20],
                    'leo': [3, 14, 25]}

for name, numbers in favorite_numbers.items():
    print(f"\n{name.title()}'s favorite_numbers are:")
    for number in numbers:
        print(f"-{number}")
