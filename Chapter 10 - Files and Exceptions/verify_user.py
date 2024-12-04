import json

def get_stored_username():
	"""Get stored username if available."""
	filename = 'username.json'
	try:
		with open(filename) as f:
			username = json.load(f)
	except FileNotFoundError:
		return None 
	else:
		return username

def get_new_username():
	"""Prompt for a new username."""
	username = input("What is your name? ")
	filename = 'username.json'
	with open(filename, 'w') as f:
		json.dump(username, f)
	return username

def greet_user():
	"""
	Greet the user by name, making sure
	that the user is matched up with the right name.
	"""
	username = get_stored_username()
	if username:
		verify_user = input(f"Is {username} the correct username? (yes/no) ")
		if verify_user == 'no':
			username = get_new_username()
		print(f"Welcome back, {username}!")
	else:
		username = get_new_username()
		print(f"We'll remember you when you come back, {username}!")

greet_user()

