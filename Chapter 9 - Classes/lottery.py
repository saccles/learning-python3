from random import choice

lottery = [1, 'a', 'd', 6, 'e', 4, 'j', 'z', 7, 3]

my_ticket = 'a16j'

# Initialize flag to break out of loop.
lottery_active = True

# Initialize loop counter. 
total_loops = 0

# Continue repeating until ticket and my_ticket
# match.
while lottery_active:
	total_loops += 1
	ticket = ''
	count = 0
	while count < 4:
		ticket += str(choice(lottery))
		count += 1
	if my_ticket == ticket:
		message = f"Winning Ticket: {ticket}"
		message += f"\nLoops: {total_loops}"
		print(message)
		lottery_active = False







