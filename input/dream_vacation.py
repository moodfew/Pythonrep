name_prompt = "What is your name? "
place_prompt = "If you could visit one place in the worls, where would you go? "
countinue_prompt = "Would you like another person take the poll? "

# Responses will be store in the form of {name: response}
responses = {}

while True:
    
    # Asking the user for information
    name = input(name_prompt)
    place = input(place_prompt)
    
    # Store the responses
    responses[name] = place
    
    # Ask if there's anyone else taking the survey
    repeat = input(countinue_prompt)
    if repeat != 'yes':
        break 

# Show result of the survey
print("\n----Survey Results----")
for name, response in responses.items():
    print(f"{name.title()} would like to go to {place.title()}.")

