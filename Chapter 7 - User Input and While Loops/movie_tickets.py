ticket_prompt = "Ticket Booth --Age Info-- \n"
ticket_prompt += "Entry is free for kids under the age of 3. \n"
ticket_prompt += "Entry is $10 for kids between the age of 3 and 12. \n"
ticket_prompt += "For kids older than 12, entry is $15. \n"
ticket_prompt += "Enter your age (type 'quit' to exit the program): "

age = ""

# While loop that repeatedly asks for a user's age and gives specific output as a result.
# Typing 'quit' ends the program.
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




