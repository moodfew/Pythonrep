filename = 'guest.txt'
prompt = 'What is your name? '

while True:
    name = input(prompt)
    
    if name != 'q':
        # Display a greeting for user and record his visit
        greeting = f"It's really nice to meet you {name.title()}!"
        print(greeting)

        record = f"{name.title()} was here."
        with open(filename, 'a') as f:
            f.write(record)

    else:
        print(f"Sorry to see you go :(")
        break

