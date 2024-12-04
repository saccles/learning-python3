filename = 'python.txt'

print("Reading an Entire File:")
with open(filename) as file_object:
	contents = file_object.read()

print(contents)

print("\nLooping Over File Object:")
with open(filename) as file_object:
	for line in file_object:
		print(line.strip())

print("\nStoring Lines in a List:")
with open(filename) as file_object:
	lines = file_object.readlines()

string = ''

for line in lines:
	string += line

print(string)
