def send_messages(messages):
	"""Move each message from one list to another list."""
	while messages:
		message = messages.pop()
		print(f"Moving '{message}' to sent_messages.")
		sent_messages.append(message)

messages = ['hey', 'how are you?', 'hi', 'lol', 'haha']
sent_messages = []

# Copies the original list, while sending the copy to the function. 
send_messages(messages[:])

print(messages)
print(sent_messages)


