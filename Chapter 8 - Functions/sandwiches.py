def get_sandwich_order(*toppings):
	"""Print a list of toppings inputted by user."""
	print(f"\nYour Sandwich Toppings: ")
	for topping in toppings:
		print(f"- {topping}")

get_sandwich_order('tomatoes')

get_sandwich_order('cheddar cheese', 'tomatoes', 'swiss cheese', 'egg')

get_sandwich_order('bacon', 'turkey')
