# Silas Accles
# 11/11/2023

# This program demonstrates how lists can be used to store and modify values.

# Part 1: Creates a list and a personal message regarding a invitation to a dinner party. 

guests = ["John Cleese", "Eric Idle", "Darth Vader", "Olaf Scholz"]

message = f"Hello {guests[0]}! Please dine with us!"
print(message)

message = f"Hello {guests[1]}! Please dine with us!"
print(message)

message = f"Hello {guests[2]}! Please dine with us!"
print(message)

message = f"Hello {guests[-1]}! Please dine with us!"
print(message)

# Part 2: Modifies the list using the insert() and append() methods to add new guests to the guest list. 

print("\nWe have found a bigger dinner table. More guests will be coming.")

guests.insert(0, "Dumbledore")
guests.insert(2, "Voldemort")
guests.append("Hermione")

message = f"Hello {guests[0]}! Please dine with us!"
print(message)

message = f"Hello {guests[1]}! Please dine with us!"
print(message)

message = f"Hello {guests[-3]}! Please dine with us!"
print(message)

message = f"Hello {guests[-2]}! Please dine with us!"
print(message)

message = f"Hello {guests[-1]}! Please dine with us!"
print(message)

# Part 3: Removes guests from the list until the list is empty. 

print("\nSorry, we can only invite two people to the dinner.")

removed_guest = guests.pop(-1)
print(f"Hey {removed_guest}, we're sorry that we cannot invite you to the dinner.")

removed_guest = guests.pop(-1)
print(f"Hey {removed_guest}, we're sorry that we cannot invite you to the dinner.")

removed_guest = guests.pop(-1)
print(f"Hey {removed_guest}, we're sorry that we cannot invite you to the dinner.")

removed_guest = guests.pop(-1)
print(f"Hey {removed_guest}, we're sorry that we cannot invite you to the dinner.")

removed_guest = guests.pop(-1)
print(f"Hey {removed_guest}, we're sorry that we cannot invite you to the dinner.")

print(f"Hey {guests[0]} and {guests[-1]}. You're still invited!")

del guests[0]
del guests[0]

print(guests)








