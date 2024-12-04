rivers = {
	'rhine': 'germany',
	'inn': 'austria',
	'nile': 'egypt',
	}

# Loops through the rivers dictionary, printing out the key (river) and value (country) pairs. 
for river, country in rivers.items():
	message = f"The {river.title()} runs through {country.title()}."
	print(message)

print("")

# Loops through the rivers dictionary, printing out the keys (river).
for river in rivers.keys():
	message = f"River: {river.title()}"
	print(message)

print("")

# Loops through the rivers dictionary, printing out the values (country).
for country in rivers.values():
	message = f"Country: {country.title()}"
	print(message)