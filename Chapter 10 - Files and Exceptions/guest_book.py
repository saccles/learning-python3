filename = 'guest_book.txt'

# Add names to a file until an exit value is specified.
while True:
	print(f"Guest Book (type 'q' to quit): ")
	name = input("Enter your name: ")
	# Allow users to quit the program. 
	if name == 'q':
		break
	print(f"Hello, {name.title()}. Welcome!")
	# Add a user's name to the file referenced by 
	# the 'filename' variable.
	with open(filename, 'a') as file_object:
		file_object.write(f"{name}\n")