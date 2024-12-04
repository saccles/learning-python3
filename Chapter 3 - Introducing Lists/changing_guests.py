# Silas Accles
# 11/11/2023

guests = ["John Cleese", "Eric Idle", "Darth Vader", "Olaf Scholz"]

# Prints that value at index 2 in list will not be come to the dinner
print(f"It's a shame that {guests[2]} cannot come to the dinner!")

# Replaces old value at given index in list
guests[2] = "Yoda"

print("Second set of dinner invitations: \n")

message = f"Hello {guests[0]}! Please dine with us!"
print(message)

message = f"Hello {guests[1]}! Please dine with us!"
print(message)

message = f"Hello {guests[2]}! Please dine with us!"
print(message)

message = f"Hello {guests[-1]}! Please dine with us!"
print(message)

print(f"Number of Guests Attending the Dinner: {len(guests)}")
