users = ['denis', 'admin', 'jonis', 'kliton', 'leonora']

if users:
    for user in users:
        if user == 'admin':
            print(f"Hello {user.title()} would you like to see a status report.")
        else:
            print(f"Hello {user.title()} thank you for logging again.")
else:
    print("We need to find some users.")
