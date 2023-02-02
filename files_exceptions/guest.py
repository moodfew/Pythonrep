filename = 'guest.txt'

prompt = 'What is your name? '
name = input(prompt)

with open(filename, 'w') as f:
    f.write(name)
