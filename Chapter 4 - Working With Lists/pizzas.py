pizzas = ["Cheese", "Pepperoni", "Pineapple"]

for pizza in pizzas:
	print(f"I like {pizza} pizza!")

print("All pizzas are great!")

friend_pizzas = pizzas[:]

pizzas.append("Vegetable")
friend_pizzas.append("Mushroom")

print("My favorite pizzas are:")

for pizza in pizzas:
	print(pizza)

print("\nMy friend's favorite pizzas are:")

for pizza in friend_pizzas:
	print(pizza)
