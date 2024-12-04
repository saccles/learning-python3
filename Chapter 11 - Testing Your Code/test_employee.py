import unittest
from employee import Employee

class EmployeeTestCase(unittest.TestCase):
	"""Tests for the class Employee."""

	def setUp(self):
		"""
		Create an employee instance and a list of new_salaries
		to choose from.
		"""
		self.employee_1 = Employee('obiwan', 'kenobi', 60000)
		self.new_salaries = [65000, 70000]

	def test_give_default_raise(self):
		"""
		Test that the default raise is correctly assigned.
		"""
		salary = self.employee_1.give_raise()
		self.assertEqual(salary, self.new_salaries[0])

	def test_give_custom_raise(self):
		"""
		Test that a custom raise is correctly assigned. 
		"""
		salary = self.employee_1.give_raise(raise_=10000)
		self.assertEqual(salary, self.new_salaries[1])

if __name__ == '__main__':
	unittest.main()



