from user import User

class Admin(User):
	"""Represent aspects of a user, specific to administrators."""

	def __init__(
			self, first_name, last_name,
			age, passion, login_attempts):
		"""
		Initialize attributes of the parent class.
		Then initialize attributes specifc to administrators.
		"""  
		super().__init__(
			first_name, last_name, age, 
			passion, login_attempts)
		self.privileges = Privileges()


class Privileges:
	"""A simple attempt to model user privileges."""

	def __init__(self):
		"""
		Initialize attributes of the parent class.
		Then initialize attributes specific to privileges.
		"""
		self.privileges = [
			'can add post', 
			'can delete post', 
			'can ban user', 
			'can edit post', 
			'can login using ssh'
			]

	def show_privileges(self):
		"""Print a list of the user's privileges."""
		privileges = f"Admin Privileges: \n{self.privileges}"
		print(privileges)

