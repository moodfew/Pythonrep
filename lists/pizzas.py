pizzas = ['Pepperoni', 'Margarita', 'Proschutte']

friend_pizzas = pizzas[:]

#for pizza in pizzas:
#    print(f"I like {pizza.title()} pizza.")

#print("\nI really like pizza.")

pizzas.append('Pineapple')
friend_pizzas.append('Eggs')

print("My pizzas:")
for pizza in pizzas:
    print(f"-{pizza}")

print("Friend's pizzas:")
for friend_pizza in friend_pizzas:
    print(f"-{friend_pizza}")
