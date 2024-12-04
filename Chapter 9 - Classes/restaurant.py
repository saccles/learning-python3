class Restaurant:
	"""A simple attempt to model a restaurant."""

	def __init__(self, restaurant_name, cuisine_type):
		"""Initialize attributes to describe a restaurant."""
		self.restaurant_name = restaurant_name.title()
		self.cuisine_type = cuisine_type.title()

	def describe_restaurant(self):
		print(f"{self.restaurant_name} offers many cuisines, including the {self.cuisine_type}.")

	def open_restaurant(self):
		print(f"\n{self.restaurant_name} is open for business.")

