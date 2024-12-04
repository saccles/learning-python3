favorite_numbers = {
	'sarah': [2, 9, 6],
	'joe': [9, 16, 14],
	'jane': [16, 3],
	'henry': [81, 2, 9] ,
	'abdul': [12, 14],
	}

for name, numbers in favorite_numbers.items():
	print(f"{name.title()}'s favorite numbers are: ")
	for number in numbers:
		print(f"\t {number}")
	print("")

