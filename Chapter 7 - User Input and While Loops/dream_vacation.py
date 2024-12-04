vacation_poll = {}

# Set a flag to indicate that polling is active.
polling_active = True

while polling_active:
	# Prompt for the person's name and dream travel destination. 
	name = input("\nWhat is your name? ")
	place = input("If you could visit one place in the world, where would you go? ")
	
	# Store the response in the dictionary. 
	vacation_poll[name] = place

	# Find out if anyone else will take the poll.
	continue_ = input("Would you like to let someone else participate in the poll? (yes/no) ")
	# Break out of the loop if someone responds with 'no.'
	if continue_ == 'no':
		polling_active = False

print("\n--- Poll Results ---")
for name, place in vacation_poll.items():
	print(f"{name.title()} would like to travel to {place.title()}.")


