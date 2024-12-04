favorite_places = {
	'jane': ['alps', 'adirondacks', 'montreat'],
	'anna': ['lakes', 'midwest'],
	'will': ['beach', 'downtown', 'riverside'],
	}

for name, places in favorite_places.items():
	print(f"{name.title()}'s favorite places are: ")
	for place in places:
		print(f"\t {place.title()}")
	print("")

