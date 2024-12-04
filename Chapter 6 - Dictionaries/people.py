person_1 = {
	'first_name': 'bill',
	'last_name': 'murphy',
	'age': '23',
	'city': 'charlotte',
    }

person_2 = {
	'first_name': 'sally',
	'last_name': 'newton',
	'age': '20',
	'city': 'boston',
    }

person_3 = {
	'first_name': 'margaret',
	'last_name': 'israel',
	'age': '27',
	'city': 'ontario',
    }

# Creates a list made up of separate dictionaries.
people = [person_1, person_2, person_3]

# Loops through the list, printing out all information about each person stored in the list.
for person in people:
	full_name = f"{person['first_name'].title()} {person['last_name'].title()}"
	age = f"{person['age'].title()}"
	city = f"{person['city'].title()}"
	print(f" Full Name: {full_name}")
	print(f" Age: {age}")
	print(f" City: {city} \n")

 