class Restaurant:
	"""A simple attempt to model a restaurant."""

	def __init__(self, restaurant_name, cuisine_type):
		"""Initialize attributes to describe a restaurant."""
		self.restaurant_name = restaurant_name.title()
		self.cuisine_type = cuisine_type.title()

	def describe_restaurant(self):
		print(f"\n{self.restaurant_name} offers many cuisines, including the {self.cuisine_type}.")

	def open_restaurant(self):
		print(f"\n{self.restaurant_name} is open for business.")

# Restaurant instances.
restaurant_1 = Restaurant('urban burrito', 'mexican cuisine')
restaurant_1.describe_restaurant()

restaurant_2 = Restaurant('homegrown', 'vegetarian cuisine')
restaurant_2.describe_restaurant()

restaurant_3 = Restaurant('chai pani', 'indian cuisine')
restaurant_3.describe_restaurant()



