prompt = "How many people are in your dinner group? "
number = input(prompt)
number = int(number)

if number > 8:
    print("You'll have to wait for a table.")
else:
    print("The table is ready.")
