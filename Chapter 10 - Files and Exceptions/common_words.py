filenames = ['grimms_fairy_tales.txt', 'gullivers_travels.txt', 'pride_and_prejudice.txt']

# Loop through all filenames in list. 
for filename in filenames:
	with open(filename, encoding='utf-8') as file_object:
		contents = file_object.read()
	# Count the number of times a word or phrase
	# appears in a file.
	word_count = contents.lower().count('the ')
	message = f"The word 'the' appears {word_count} "
	message += f"times in {filename}."
	print(message)