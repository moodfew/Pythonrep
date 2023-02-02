current_users = ['day', 'moodfew', 'goofy', 'ganiu', 'adc']

new_users = ['ganiu', 'patric', 'goofy', 'thor', 'goku']

current_users_lower = [user.lower() for user in current_users]

for username in new_users:
    if username.lower() in current_users:
        print(f"The {username} username is already taken.")
    else:
        print(f"The {username} username is available")
