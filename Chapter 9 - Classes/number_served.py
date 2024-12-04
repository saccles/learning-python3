class Restaurant:
	"""A simple attempt to model a restaurant."""

	def __init__(self, restaurant_name, cuisine_type):
		"""Initialize attributes to describe a restaurant."""
		self.restaurant_name = restaurant_name.title()
		self.cuisine_type = cuisine_type.title()
		self.number_served = 0

	def describe_restaurant(self):
		print(f"\n{self.restaurant_name} offers many cuisines, including the {self.cuisine_type}.")

	def open_restaurant(self):
		print(f"\n{self.restaurant_name} is open for business.")

	def set_number_served(self, number):
		self.number_served = number

	def read_number_served(self):
		print(f"As of now, {self.number_served} customers have been served.")

	def increment_number_served(self, increment):
		self.number_served += increment

restaurant = Restaurant('urban burrito', 'mexican cuisine')
restaurant.read_number_served()

restaurant.number_served = 15
restaurant.read_number_served()

restaurant.set_number_served(18)
restaurant.read_number_served()

restaurant.increment_number_served(41)
restaurant.read_number_served()


