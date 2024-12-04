def show_messages(messages):
	"""Display inputted messages."""
	counter = 1
	for message in messages:
		print(f"Message #{counter}: {message}")
		counter += 1

messages = ['hey', 'how are you?', 'hi', 'lol', 'haha']
show_messages(messages)


