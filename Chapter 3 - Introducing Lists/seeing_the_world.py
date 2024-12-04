# Silas Accles
# 11/11/2023

# This program uses the sorted() function and various methods to modify the order of a list's items.

locations = ["Innsbruck", "Zurich", "Adirondacks", "Bregenz", "Munich"]

print(f"Original Order: \n\t {locations}")

print(f"Alphabetical Order: \n\t {sorted(locations)}")

print(f"Current Order: \n\t {locations}")

locations.reverse()
print(f"New Reverse Order: \n\t {locations}")

# Uses the reverse() method a second time to print the list in its original order.  
locations.reverse()
print(f"Original Order: \n\t {locations}")

locations.sort()
print(f"New Alphabetical Order: \n\t {locations}")

locations.sort(reverse=True)
print(f"New Reverse-Alphabetical Order: \n\t {locations}")




