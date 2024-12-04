def describe_city(city, country='germany'):
	print(f"{city.title()} is in {country.title()}.")

# Default 'country' parameter, user-selected city.
describe_city('heidelberg')

# Only user-selected arguments (for below function-calls).
describe_city('innsbruck', country='austria')

describe_city('london', country='england')

