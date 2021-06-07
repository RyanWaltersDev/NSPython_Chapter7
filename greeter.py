#!/usr/bin/env python3
# RyanWatlersDev Jun 7 2021 -- Messing with prompts

'''
# Initial prompt
name = input("Please enter your name: ")
print(f"\nHello, {name}!")
'''

# Prompt with multiple lines
prompt = "If you tell us who you are, we can personalize the messages for you."
prompt += "\nWhat is your first name? "

name = input(prompt)
print(f"\nHello, {name}!")

# END OF PROGRAM