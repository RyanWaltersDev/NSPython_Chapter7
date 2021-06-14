#!/usr/bin/env python3
# RyanWaltersDev Jun 14 2021 -- introducing the break statement

# Initial prompt
prompt = "\nPlease enter the name of a city you have visited: "
prompt += "\n(Enter 'quit' when you are finished.) "

# While loop with break
while True:
    city = input(prompt)

    if city == 'quit':
        break
    else:
        print(f"{city.title()} looks beautiful! I'd love to go some day.")

# END OF PROGRAM
