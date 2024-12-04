import json

def store_favorite_number():
	"""Read and store a favorite number."""
	filename = 'favorite_number.json'
	favorite_number = input("What is your favorite number? ")
	with open(filename, 'w') as file_object:
		json.dump(favorite_number, file_object)

# Print a user's previously chosen favorite number.
def print_favorite_number():
	"""
	Tell the user their previously stored
	favorite number.
	"""
	filename = 'favorite_number.json'
	with open(filename) as file_object:
		favorite_number = json.load(file_object)
	message = f"I know your favorite number! "
	message += f"It's {favorite_number}."
	print(message)

store_favorite_number()
print_favorite_number()