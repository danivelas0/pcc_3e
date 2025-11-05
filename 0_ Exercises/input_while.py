# Rental_car

car_type = input("What brand of car would you like to rent?:")
print(f"Let me see if I can find you a {car_type}")

# restaurant_seating

number_of_people = int(
    input("How many people are there in your dinner group?:"))

if number_of_people > 8:
    print("You have to wait for a table")
else:
    print("Your table is ready")

# Pizza_toppings

pizza_topping = 'Enter a pizza topping:'
pizza_topping += "\n(type 'quit' to exit)"

message = ''

while True:
    message = input(pizza_topping)
    if message.lower() == 'quit':
        break
    else:
        print('This topping will be added to your pizza\n')

# Movie_Tickets

prompt = prompt = "Please type your age (or type 'quit' to exit): "
message = ''
age = ''

while True:
    message = input(prompt)
    if message.lower() == 'quit':
        break
    age = int(message)
    if age < 3:
        print("Your ticket is free!")
    elif age < 13:
        print('Your ticket is $10')
    else:
        print('Your ticket is $15')
