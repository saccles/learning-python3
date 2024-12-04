topping = "Enter another pizza topping. \n"
topping += "Type 'quit' to exit the program. "

next_topping = ""
while next_topping != 'quit':
	next_topping = input(topping)
	if next_topping != 'quit':
		print(f"Adding {next_topping.title()} to your pizza. \n")