#!/usr/bin/env python3
# RyanWaltersDev Jun 14 2021 -- Flag with while loop

# Initial prompt
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "

# Flag and while loop
active = True
while active:
    message = input(prompt)
    # If statement for flag
    if message == 'quit':
        active = False
    else:
        print(message)


# END OF PROGRAM
