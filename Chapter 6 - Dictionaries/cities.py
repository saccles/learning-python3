# Creates a nested dictionary, a dictionary made up of dictionaries, containing different cities and general city details. 
cities = {
	'heidelberg': {
		'country': 'germany',
		'population': '177190',
		'fact': 'located along the neckar river',
		},

	'innsbruck': {
		'country': 'austria',
		'population': '311000',
		'fact': 'capital of austrian province tirol',
		},

	'freiburg': {
		'country': 'germany',
		'population': '230000',
		'fact': 'located in the southern black forest',
		},
		
	}

# Loops through the nested dictionary, printing out city names and information about each city.  
for city, details in cities.items():
	print(f"{city.title()} Facts and Figures: ")
	country = f"{details['country'].title()}"
	population = f"{details['population']}"
	fact = f"{details['fact'].title()}"

	print(f"\t Country: {country}")
	print(f"\t Population: {population}")
	print(f"\t Fact: {fact} \n")
