pet_1 = {
	'animal_type': 'dog',
	'owner_name': 'joe',
	}

pet_2 = {
	'animal_type': 'cat',
	'owner_name': 'will',
	}

pet_3 = {
	'animal_type': 'snake',
	'owner_name': 'isabella',
	}

pet_4 = {
	'animal_type': 'bird',
	'owner_name': 'maurice',
	}

pet_5 = {
	'animal_type': 'hamster',
	'owner_name': 'susan',
	}

# Creates a list of pets, with each pet being its own separate dictionary.
pets = [pet_1, pet_2, pet_3, pet_4, pet_5]

# Loops through the pet list, printing out all avialable information. 
for pet in pets:
	animal_type = f"{pet['animal_type'].title()}"
	owner_name = f"{pet['owner_name'].title()}"
	print(f"Kind of Animal: {animal_type}")
	print(f"Owner's Name: {owner_name} \n")