# If Statements

# Conditional Statements
# = single equal sign is a statement.
# == double equal sign asks a question.

cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
    if car == 'bww':  # is the value of car equal to 'bwm'?
        print(car.upper())  # conditional statement
    else:
        print(car.title())

car = 'Audi'  # Assign the capitalized sting 'Audi' to the variable car.
# converts the variable to lower case before doing the test.
car.lower() == 'audi'

# Checking inequality

pizza_toppings = ['mushrooms', 'pepperonni', 'cheddar cheese']
for pizza_topping in pizza_toppings:
    if pizza_topping != 'anchovies':  # not equal
        print('Hold the anchovies')
    else:
        print('I love anchovies')
# Numerical Comparisons
answer = 17
if answer != 42:
    print('That is not the correct answer. Please try again!')

# Multiple Conditions
# and / or statements

age_0 = 22
age_1 = 18

# Evaluates to False if one of the expressions fail.
if age_0 >= 21 and age_1 >= 21:
    print('You\'re allowed')
else:
    print('You\'re Fired!')

# or statement evaluates to False if both expressions fail.

age_0 = 18
age_1 = 18
if age_0 >= 21 or age_1 >= 21:
    print('True')
else:
    print('False')

# in, is not in a list
pizza_toppings = ['mushrooms', 'onions', 'pineapple']
'mushrooms' in pizza_toppings  # True

# BOOLEAN EXPRESSIONS
# Boolean values provide an efficient way to track the state of a program or a particular condition that is important in your program.

game_active = True
can_edit = False

# EXERCISES
weather = 'summer'
if weather == 'summer':
    print('Let\'s go to the beach')

weather = 'winter'
if weather != 'summer':
    print('I don\'t like this weather. I rather prefer summer!.')

cars = ['BMW', 'Audi', 'Mercedes', 'Lexus', 'Porsh']

for car in cars:
    # turn variable value into lowercase before checking the condition.
    if car.lower() == 'bmw':
        print('This is my favorite brand car')
    else:
        print('This brand sucks')

year_born = 2000
if year_born >= 2000:
    print('You\'re a Gen Z')
else:
    print('You\'re Old')

emotion_1 = 'love'
emotion_2 = 'friendship'
emotion_3 = 'lover'

if emotion_1 == 'love' and emotion_2 == 'friendship' and emotion_3 == 'lover':
    print('We can marry Honey!')
else:
    print('Let\'s just be friends!.')

emotion_1 = 'happy'
emotion_2 = 'fit'

if emotion_1 == 'fat' or emotion_2 == 'sad':
    print('Go to the fucking gym')
else:
    print('Keep going to the fucking gym')

# EXERCISES
alien_color = 'green'
if alien_color == 'green':
    print('You just earned 5 miserable points')
else
print('You just earned 10 good points')

alien_color = 'red'
if alien_color == 'green':
    print('You just earned 5 points')
elif alien_color == 'yellow':
    print('You just earned 10 ')
elif alien_color == 'red':
    print('You just earned 15 points')

# stages of life
age = 13
if age < 2:
    print('You\'re a baby')
elif age >= 4 and age < 13:
    print('You\'re a kid')
elif age >= 13 and age < 20:
    print('You\'re a teen')
elif age >= 20 and age < 65:
    print('You\'re an Adult')
else:
    print('You\'re a Senior')

# favorite_fruits

favorite_fruits = ['Orange', 'Blueberries', 'Mango']
if 'Orange' in favorite_fruits:
    print('You really like Oranges')
if 'Blueberries' in favorite_fruits:
    print('You really like Blueberries')
if 'Mango' in favorite_fruits:
    print('You really like Mango')
print('\nJust keep eating fruits bastard!')

# EXERCISES

users = ['Paola', 'Elisa', 'Ariana', 'Jose', 'Antonio', 'Admin']
if users:
    for user in users:
        if user == 'Admin':
            print('Welcome again Admin, do you want to see a status report?')
        else:
            print(f'Hello {user},thank you for logging in again.')
else:
    print('We need to find some users')

# Checking usernames

current_users = ['Paola', 'Elisa', 'Ariana', 'Jose', 'Antonio']
new_users = ['Pedro', 'Jomar', 'pelo_liso', 'Paola1']

current_users_lowercase = []
for current_user in current_users:
    current_users_lowercase.append(current_user.lower())

for new_user in new_users:
    if new_user.lower() in current_users_lowercase:
        print(f'Sorry, {new_user}, this username is already in use')
    else:
        print(f'Welcome!,{new_user}')

# Ordinal_Numbers

ordinal_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for ordinal_number in ordinal_numbers:
    if ordinal_number == 1:
        print(f'{ordinal_number}st')
    elif ordinal_number == 2:
        print(f'{ordinal_number}nd')
    elif ordinal_number == 3:
        print(f'{ordinal_number}rd')
    else:
        print(f'{ordinal_number}th')
