def make_shirt(size, message):
	print(f"You have chosen a {size} shirt.")
	print(f"The message on your shirt is '{message}' \n")

# Positional Arguments
make_shirt('small', 'Make sure the prince does not leave the room until I come and get him')

# Keyword Arguments
make_shirt(message='Make sure the prince does not leave the room until I come and get him', size='small')