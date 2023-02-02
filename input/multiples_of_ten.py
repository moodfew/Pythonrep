prompt = "Tell me a number and I'll check if it's a multiple of 10. "
number = input(prompt)
number = int(number)

if number % 10 == 0:
    print(f"The number {number} is a multiple of 10.")
else:
    print(f"The number {number} is not a multiple of 10.")
