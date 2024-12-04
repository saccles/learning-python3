filename = 'programming_poll.txt'

# Add names to a file until an exit value is specified.
while True:
	print(f"---Programming Poll--- \n(type 'q' to quit): ")
	reason = input("What do you like about programming? ")
	# Allow users to quit the program. 
	if reason == 'q':
		break
	print(f"Thanks for responding to the poll!\n")
	# Add a user's reason to the file referenced by 
	# the 'filename' variable.
	with open(filename, 'a') as file_object:
		file_object.write(f"{reason}\n")