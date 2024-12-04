sandwich_orders = ['peanut_butter', 'cream_cheese', 'cheese', 'turkey', 'fish']
finished_sandwiches = []

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
