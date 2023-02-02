favorite_places = {
        'denis': ['karaburun', 'backrooms', 'llogora'],
        'goofy': ['germany', 'france'],
        'dawg': ['nigeria', 'mexico'],
        }

for name, places in favorite_places.items():
    print(f"{name.title()}'s favorite places are:")
    for place in places:
        print(f"-{place.title()}")

