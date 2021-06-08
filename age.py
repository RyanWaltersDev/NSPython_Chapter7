#!/usr/bin/env python3
# RyanWaltersDev Jun 7 2021 -- integers as user inputs

# Return age as a string
'''
age = input("How old are you? ")
print(age)
'''

# Purposeful error, string cannot compare to int
'''
age = input("How old are you? ")
if age >= 18:
    print("You are old enough to vote!")
'''

# Fix error by int(function)
age = input("How old are you? ")
age = int(age)
if age >= 18:
    print("You are old enough to vote!")
else:
    print("Sorry, you are not old enough to vote.")

# END OF PROGRAM
