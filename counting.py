#!/usr/bin/env python3
# RyanWaltersDev Jun 9 2021 -- while loop and continue statement

# Initial number and input
current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1

# Count to 10 only odd
current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue
    print(current_number)

# Avoid infinite loop
x = 1
while x <= 5:
    print(x)
    # Without this next line, the loop runs forever!
    x += 1

# END OF PROGRAM
