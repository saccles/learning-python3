dinner_group = input("How many people are in your dinner group? ")
dinner_group = int(dinner_group)

if dinner_group > 8:
	print("I am sorry. You will have to wait for a table.")
else: 
	print("Your table is ready!")