favorite_languages = {
	'jen': 'python',
	'sarah': 'c',
	'edward': 'ruby',
	'phil': 'python',
	}

people_to_poll = ['sarah', 'jen', 'joe', 'abdul', 'anna']

for person in people_to_poll:
	if person in favorite_languages.keys():
		print(f"{person.title()}, thank you for responding to our poll!")
	else:
		print(f"{person.title()}, please consider responding to our poll!")
