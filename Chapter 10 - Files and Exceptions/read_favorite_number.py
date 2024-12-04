import json

filename = 'favorite_number.json'

favorite_number = input("What is your favorite number? ")

with open(filename, 'w') as file_object:
	json.dump(favorite_number, file_object)