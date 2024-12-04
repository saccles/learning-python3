print("---Number Addition---")

first_number = input("Enter the first number: ")
second_number = input("Enter the second number: ")

try:
	# Add up the first and second numbers.
	result = int(first_number) + int(second_number)
except ValueError:
	message = "You can only enter numbers!"
	message += "\nTry again."
	print(message)
else:
	print(f"{first_number} + {second_number} = {result}")