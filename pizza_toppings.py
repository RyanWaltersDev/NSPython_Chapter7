#!/usr/bin/env python3
# RyanWaltersDev Jun 14 2021 -- TIY 7-4

# Initial prompt
prompt = "\nWelcome to Pizza Parlour! \n(Enter 'quit' to close program)"
prompt += "\nWhat would you like on your pizza? "

# while loop
topping = ""
while topping.title() != 'Quit':
    topping = input(prompt)
    if topping.title() != 'Quit':
        print(f"Ok, we will add {topping}.")

#END OF PROGRAM
