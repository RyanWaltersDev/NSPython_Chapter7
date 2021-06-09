#!/usr/bin/env python3
# RyanWaltersDev Jun 8 2021 -- User input TIY 7-1

# Input variable
rental = input("What kind of car would you like to rent today? ")
print(f"Ok, let me see if we have a {rental.title()} available for rent!")
 
# List of available cars
rental_inventory = ['Subaru', 'Kia', 'Ford', 'Toyota']

# if-else to determine if request can be fulfilled
if rental.title() in rental_inventory:
    print(f"\nGreat news! We have a {rental.title()} available!")
else:
    print(f"\nI am very sorry, but we do not have a "
        f"{rental.title()} available.")

# END OF PROGRAM
