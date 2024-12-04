import json

filename = 'favorite_number.json'

with open(filename) as file_object:
	favorite_number = json.load(file_object)
message = f"I know your favorite number! "
message += f"It's {favorite_number}."
print(message)