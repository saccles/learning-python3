def get_city_country(city, country, population=None):
	"""
	Return a single string of the form City, Country
	Ex: Santiago, Chile.
	"""
	if population:
		city_country = f"{city}, {country} - Population {population}"
	else:
		city_country = f"{city}, {country}"
	return city_country.title()
	
