class Employee:
	"""A simple attempt to model an employee."""

	def __init__(self, first_name, last_name, salary):
		"""Initialize attributes of an employee."""
		self.first_name = first_name
		self.last_name = last_name
		self.salary = salary

	def give_raise(self, raise_=5000):
		"""
		Give an employee a default raise or a custom raise.
		"""
		self.salary += raise_
		return self.salary

	