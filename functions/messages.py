def show_messages(messages):
    """Printing all messages"""

    print("Showing all messages")
    for message in messages:
        print(message)

def send_messages(messages, sent_messages):
    """Print each message and move it to sent_messages"""

    print("\nSending all messages:")
    while messages:
        current_message = messages.pop()
        print(current_message)
        sent_messages.append(current_message)

messages = ['hey', 'what', 'good', 'hello', 'tomorrow', 'ok']
show_messages(messages)

sent_messages = []
send_messages(messages, sent_messages)

print("\nFinal list:")
print(messages)
print(sent_messages)
