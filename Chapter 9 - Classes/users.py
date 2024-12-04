class User:
	"""A simple attempt to model a user."""

	def __init__(self, first_name, last_name, age, passion):
		"""Initialize attributes to describe a user."""
		self.first_name = first_name.title()
		self.last_name = last_name.title()
		self.age = age
		self.passion = passion

	def describe_user(self):
		full_name = f"{self.first_name} {self.last_name}"
		print(f"Full Name: {full_name}")
		print(f"Age: {self.age}")
		print(f"Passion: {self.passion}")

	def greet_user(self):
		print(f"Hello {self.first_name}, it's good to see you!\n")

# User instances.
user_1 = User('luke', 'skywalker', '21', 'jedi mind tricks')
user_1.describe_user()
user_1.greet_user()

user_2 = User('harry', 'potter', '17', 'dark-wizard hunting')
user_2.describe_user()
user_2.greet_user()

user_3 = User('susan', 'sto-helit', '24', 'supernatural activities')
user_3.describe_user()
user_3.greet_user()

