#!/usr/bin/env python3
# RyanWaltersDev Jun 9 2021 -- User input TIY 7-2

# Initial input and convert to integer
seating = input("Hello, and welcome to Metropolis! How many in your party? ")
seating = int(seating)

# If-else to determine if seating is avaiable
print(f"\n{seating}? Alright, let me check our availability.")
if seating > 8 and seating < 20:
    print(f"\nNo problem. Give us a few more minutes to get your table ready.")
elif seating > 20:
    print(f"\nMy deepest apologies, we cannot accept parties of more than "
        "20 without prior notice.")
else:
    print(f"\nExcellent! We have a table ready for you now. Right this way.")

# END OF PROGRAM
