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


class IceCreamStand(Restaurant):
	"""Represent aspects of a restaurant, specific to ice cream stands."""

	def __init__(self, restaurant_name, cuisine_type, flavors):
		"""
		Initialize attributes of the parent class.
		Then initialize attributes specifc to ice cream stands.
		"""
		super().__init__(restaurant_name, cuisine_type)
		self.flavors = flavors

	def show_flavors(self):
		"""Print a list of ice cream flavors."""
		flavors = f"List of Ice Cream Flavors: \n{self.flavors}"
		print(flavors)

ice_cream_stand_1 = IceCreamStand('the hop', 'homemade cones', ['vanilla', 'chocolate', 'strawberry', 'banana'])
ice_cream_stand_1.show_flavors()