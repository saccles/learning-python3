current_users = ['temPest', 'bILl44', 'Sh@dow', 'aDMIn', 'Joe']

current_users_lower = []

# Copies item from current_users to current_users_lower, making sure each new item is stored in lowercase.
for user in current_users:
	user = user.lower()
	current_users_lower.append(user)

new_users = ['gale', 'BILL44', 'whirlwind', 'rebecca', 'SH@doW']

# Loops through new_users list. 
# Checks if the user in new_users is already in current_users. 
# If this is the case, the program prints a message that the selected username is unavilable. 
for user in new_users:
	if user.lower() in current_users_lower:
		print(f"Sorry. {user} is not available. Please pick another name.")
	else:
		print(f"The name '{user}' is available. Welcome!")

