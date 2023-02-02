def make_sandwich(*toppings):
    """Summary of the sandwich"""

    print("\nMaking a sandwich with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")

make_sandwich('eggs', 'pepperoni', 'cheese')
make_sandwich('olives', 'sallami', 'bacon', 'cheese')
make_sandwich('chicken', 'vegtables')
