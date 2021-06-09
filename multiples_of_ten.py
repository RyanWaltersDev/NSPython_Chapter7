#!/usr/bin/env python3
# RyanWaltersDev Jun 9 2021 -- User input 7-3

# Initial input
number = input("Give me a number, and I will tell you if it is "
    "divisible by 10! ")
number = int(number)

# If-else to determine divisibility 
if number % 10 == 0:
    print(f"\nThe number {number} is divisible by 10!")
else:
    print(f"\nThe number {number} is not divisible by 10.")

# END OF PROGRAM
