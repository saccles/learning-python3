filename = 'python.txt'

# Open python.txt for read operations and read entire file.
with open(filename) as file_object:
	contents = file_object.read()

print(f"Original Contents:\n{contents}\n")

# Replace 'python' with 'C'.
contents = contents.replace('python', 'C')
print(f"Modified Contents:\n{contents}")