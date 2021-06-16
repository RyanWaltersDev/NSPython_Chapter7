#!/usr/bin/env python3
# RyanWaltersDev Jun 16 -- Removing specific values

# Initial list and print
pets = ['dog', 'cat', 'dog', 'hamster', 'rabbit', 'cat', 'dog', 'goldfish']
print(pets)

# while loop to remove all instances of dog
while 'dog' in pets:
    pets.remove('dog')

# Print final list
print(pets)

#END OF PROGRAM
