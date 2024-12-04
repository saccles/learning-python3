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
