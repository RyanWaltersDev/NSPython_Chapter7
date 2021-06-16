#!/usr/bin/env python3
# RyanWaltersDev Jun 16 2021 -- TIY 7-8 and 7-9

# Initial list
sandwich_orders = [
    'pastrami', 'italian', 'ham', 'capricolla', 
    'pastrami', 'meatball', 'grilled chicken', 'pastrami',
    ]
finished_sandwiches = []

# Remove pastrami 7-9
print("My apologies, we are out of pastrami! But the other sandiwches "
    "will be ready shortly.")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

# While loop
while sandwich_orders:
    finished_sandwich = sandwich_orders.pop()
    print(f"We finished making your {finished_sandwich.title()} Sandwich!")
    finished_sandwiches.append(finished_sandwich)

# Print List
print("\nHere is the full order of sandwiches that we made for you.")
for sandwich in finished_sandwiches:
    print(sandwich.title())

# END OF PROGRAM
