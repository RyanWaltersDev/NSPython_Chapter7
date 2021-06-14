#!/usr/bin/env python3
# RyanWaltersDev Jun 3 2021 -- Initial input() test

# Input message
'''
message = input("Tell me something, and I will repeat it back to you: ")
print(message)
'''

# New input message
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "

# while loop -- user input quit
message = ""
while message != 'quit':
    message = input(prompt)
    # If statement so that quit does not print
    if message != 'quit':
        print(message)

# END OF PROGRAM
