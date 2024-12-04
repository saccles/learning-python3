def get_city_country(city, country):
	"""Return a city, country string that is neatly formatted."""
	formatted_string = f"{city}, {country}"
	return formatted_string.title()

# Function Call 1
city_country = get_city_country('santiago', 'chile')
print(city_country)

# Function Call 2
city_country = get_city_country('heidelberg', 'germany')
print(city_country)

# Function Call 3
city_country = get_city_country('zurich', 'switzerland')
print(city_country)

