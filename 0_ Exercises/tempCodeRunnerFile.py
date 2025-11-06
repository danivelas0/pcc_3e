poll = {}

# setting flag
polling_active = True

while polling_active:
    name = input('\nWhat is your name?')
    response = input(
        '\nif you could visit one place in the world, where would yo go?')

    # store response in the dictionary
    poll[name] = response

    # Find out if anyone else is going to take the poll.
    repeat = input("Would you like to let another person respond? (yes/ no) ")
    if repeat == 'no':
        polling_active = False

# Polling is complete. Show the results.
print("\n--- Poll Results ---")
for name, response in poll.items():
    print(f"{name} would like to go to: {response}.")