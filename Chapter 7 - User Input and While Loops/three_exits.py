ticket_prompt = "Ticket Booth --Age Info-- \n"
ticket_prompt += "Entry is free for kids under the age of 3. \n"
ticket_prompt += "Entry is $10 for kids between the age of 3 and 12. \n"
ticket_prompt += "For kids older than 12, entry is $15. \n"
ticket_prompt += "Enter your age (type 'quit' to exit the program): "



# Exiting the Loop By Using a Conditional Statement
age = ""

while age != 'quit':
	age = input(ticket_prompt)

	if age != 'quit':
		age = int(age)

		if age < 3:
			print("Your ticket is free. \n")
		elif age >= 3 and age <= 12:
			print("Your ticket is $10. \n")
		elif age > 12:
			print("Your ticket is $15. \n")

# Using an Active Variabe to Control the Loop
active = True

while active:
	age = input(ticket_prompt)

	if age == 'quit':
		active = False
	elif age != 'quit':
		age = int(age)

		if age < 3:
			print("Your ticket is free. \n")
		elif age >= 3 and age <= 12:
			print("Your ticket is $10. \n")
		elif age > 12:
			print("Your ticket is $15. \n")

# Using Break to Control the Loop
while True:
	age = input(ticket_prompt)
	if age == 'quit':
		break
	age = int(age)
	
	if age < 3:
		print("Your ticket is free. \n")
	elif age >= 3 and age <= 12:
		print("Your ticket is $10. \n")
	elif age > 12:
		print("Your ticket is $15. \n")

