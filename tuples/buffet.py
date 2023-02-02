foods = ('eggs', 'pasta', 'patatoes', 'meat', 'soup')

print("Restaurant basic menu:")
for food in foods:
    print(f"-{food.title()}")

# THe Restaurant changed it's menu
foods = ('eggs', 'pasta', 'soup', 'rice', 'chicken')

print("\nRevised basic menu:")
for food in foods:
    print(f"-{food}")
