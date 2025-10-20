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
