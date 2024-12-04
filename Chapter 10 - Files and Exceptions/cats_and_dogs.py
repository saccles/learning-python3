filenames = ['cats.txt', 'dogs.txt']

for filename in filenames:
	try:
		# Read a file and store its contents in a variable.
		with open(filename) as file_object:
			contents = file_object.read()
	except FileNotFoundError:
		print(f"Sorry, the file {filename} does not exist.")
	else:
		# Print a file's contents. 
		print(f"Contents of {filename}:\n{contents}\n")

