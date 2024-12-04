def make_shirt(size='large', message='I love Python'):
	print(f"You have chosen a {size} shirt.")
	print(f"The message on your shirt is '{message}' \n")

# Default Arguments
make_shirt()

# 'message' parameter left at default value,
# 'size' argument chosen by user.
make_shirt(size='medium')

# User-Selected Arguments
make_shirt(message ='Your mother was a hamster', size='small')