
# Loop through code until a user specifies a quit value.
while True:
	print("\n---Number Addition---")
	print("(enter 'q' to quit)")
	first_number = input("Enter the first number: ")
	if first_number == 'q':
		break
	second_number = input("Enter the second number: ")
	if second_number == 'q':
		break
	try:
		# Add up the first and second numbers.
		result = int(first_number) + int(second_number)
	except ValueError:
		message = "You can only enter numbers!"
		message += "\nTry again."
		print(message)
	else:
		print(f"{first_number} + {second_number} = {result}")