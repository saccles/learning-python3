from random import randint

class Die:
	"""Doc-String Place Holder"""

	def __init__(self, sides=6):
		"""Doc-String Place Holder"""
		self.sides = sides

	def roll_die(self):
		"""Doc-String Place Holder"""
		number = randint(1, (self.sides))
		return number

my_dice = Die(20)

for number in range(1, 11):
	nextNumber = my_dice.roll_die()
	print(f"(Roll #{number} \nNumber: {nextNumber}")
