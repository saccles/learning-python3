sandwich_orders = ['pastrami', 'peanut_butter', 'pastrami', 'cream_cheese', 'cheese', 'turkey', 'fish', 'pastrami']
finished_sandwiches = []

print("The deli has run out of pastrami sandwiches.")

# Remove every occurence of 'pastrami' from sandwich_orders. 
while 'pastrami' in sandwich_orders:
	sandwich_orders.remove('pastrami')

# Move each sandwich from sandwich_orders to finished_sandwiches (different lists) 
# until sandwich_orders is empty.
while sandwich_orders:
	current_sandwich = sandwich_orders.pop()
	print(f"I made your {current_sandwich.title()} sandwich.")
	finished_sandwiches.append(current_sandwich)

# Print each finished sandwich.
print("Finished Sandwiches:")
for sandwich in finished_sandwiches:
	print(sandwich.title())
