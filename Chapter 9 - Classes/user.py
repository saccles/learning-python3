class User:
	"""A simple attempt to model a user."""

	def __init__(
			self, first_name, last_name,
			age, passion, login_attempts):
		"""Initialize attributes to describe a user."""
		self.first_name = first_name.title()
		self.last_name = last_name.title()
		self.age = age
		self.passion = passion
		self.login_attempts = login_attempts

	def describe_user(self):
		full_name = f"{self.first_name} {self.last_name}"
		print(f"Full Name: {full_name}")
		print(f"Age: {self.age}")
		print(f"Passion: {self.passion}")

	def greet_user(self):
		print(f"Hello {self.first_name}, it's good to see you!\n")

	def increment_login_attempts(self):
		"""Increment login_attempts by 1."""
		self.login_attempts += 1

	def reset_login_attempts(self):
		self.login_attempts = 0