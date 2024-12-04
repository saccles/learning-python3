def send_messages(messages, sent_messages):
	"""Move each message from one list to another list."""
	print("---Message Sender---")
	while messages:
		message = messages.pop()
		print(f"Moving '{message}' to sent_messages.")
		sent_messages.append(message)


def show_sent_messages(messages):
	print("\n---Message Receiver---")
	"""Display sent messages."""
	counter = 1
	for message in messages:
		print(f"Message #{counter}: {message}")
		counter += 1



