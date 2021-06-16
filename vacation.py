#!/usr/bin/env python3
# RyanWaltersDev Jun 16 2021 -- TIY 6-10

# Set flag and empty dict
polling_active = True
responses = {}

# While loop with prompts
while polling_active:
    name = input("\nWhat is your name? ")
    response = input("If you could go anywhere in the world for a "
        "two week vacation, where would it be? ")

    # Define dictionary
    responses[name] = response

    # Ask to continue
    repeat = input("Would you like to let another person respond? (yes / no) ")
    if repeat == 'no':
        polling_active = False

# Results
print("\n--- Poll Results! ---")
for name, response in responses.items():
    print(f"{name.title()} wants to go to {response.title()}! Cool!")

# END OF PROGRAM
