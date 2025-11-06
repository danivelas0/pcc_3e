# Exercises
# 7-8, 7-9
sandwich_orders = ['pastrami', 'shawarma', 'cheesesteak',
                   'tuna', 'madame', 'pastrami', 'pastrami']
finished_sandwiches = []

print("I'm sorry, we're all out of pastrami today.")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(f"\nYour {current_sandwich} sandwich is been prepared!")
    finished_sandwiches.append(current_sandwich)

# Display all
print('\n---This sandwiches has been Cooked---')
for finish_sandwich in finished_sandwiches:
    print(finish_sandwich.title())

# Dream_Vacation

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
