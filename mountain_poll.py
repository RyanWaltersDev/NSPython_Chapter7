#!/usr/bin/env python3
# RyanWaltersDev Jun 16 2021 -- Filling a dictionary with user input

# Empty dictionary
responses = {}

# Set a flag to indicate that polling is active.
polling_active = True

while polling_active:
    #Prompt for the person's name and response
    name = input("\nWhat is your name? ")
    response = input("\nWhich mountain would you like to climb some day? ")

    # Store the response in a dictionary
    responses[name] = response

    # Find out if anyone else is going to take the poll
    repeat = input("Would you like to let another person respond? (yes / no) ")
    if repeat == 'no':
        polling_active = False

# Polling is complete. Print the results.
print("\n--- Poll Results ---")
for name, response in responses.items():
    print(f"{name} would like to climb {response}.")

# END OF PROGRAM
