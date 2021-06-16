#!/usr/bin/env python3
# RyanWaltersDev Jun 16 2021 -- moving lists with while loop

# Initial lists
uncomfirmed_users = ['mike', 'jen', 'david', 'candace']
confirmed_users = []

# Verify each user until there are no more confirmed users.
# Move each verified user into the list of confirmed users.
while uncomfirmed_users:
    current_user = uncomfirmed_users.pop()
    print(f"Verifying user: {current_user.title()}")
    confirmed_users.append(current_user)

# Display all confirmed users.
print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())

# END OF PROGRAM
