file_name = 'poll_responses.txt'

# Preparing the prompts
question_prompt = 'Why do you like programming? '
continue_prompt = 'Would you like another person to take the poll? (yes/no) '

# Empty list to store the responses
responses = []

while True:
    # Appending each response by user to empty list
    response = input(question_prompt)
    responses.append(response)
    
    # Looking if anyone else is taking the poll
    continue_poll = input(continue_prompt)
    if continue_poll != 'yes':
        break

# Writing responses to file_name
with open(file_name, 'a') as f:
    for response in responses:
        f.write(f"{response}\n")

