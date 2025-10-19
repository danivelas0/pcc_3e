# Looping Through an Entire List
# You can loop through all the items in a list using a for loop.

magicians = ['alice', 'david', 'carolina']  # define a list
# This line tells Python to pull a name from the list magicians, and associate it with the variable magician.
for magician in magicians:
    print(magician)  # print each item in the list
# “For every magician in the list of magicians, print the magician’s name.”

# keep in mind when writing your own for loops that you can choose
# any name you want for the temporary variable that will be associated with
# each value in the list. However, it’s helpful to choose a meaningful name that
# represents a single item from the list. For example, here’s a good way to start

# a for loop for a list of cats, a list of dogs, and a general list of items:
# for cat in cats:
# for dog in dogs:
# for item in list_of_items:

magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(f"{magician.title()},that was a wonderful trick!")
    print(f"I can't wait to see your next trick, {magician.title()}.\n")

# this line is not part of the for loop.
print("Thank you, everyone. That was a great magic show!")

pizzas = ['pepperoni', 'mushrooms', 'all the meats',
          "triple cheese", "napoletana", "bbq chicken"]
for pizza in pizzas:
    print(f"I like {pizza} pizza.")
print("I really love pizza!")

# MAKING NUMERICAL LISTS

# Use the range() function to work with a set of numbers in a for loop.

for value in range(1, 5):
    print(value)
# The range() function starts at the first number you give it, and stops just before the second number you provide.
# So range(1, 5) tells Python to count from 1 to 4
# (and not include 5 in the set of numbers it generates).
# If you want to count to 5, you need to tell Python to go one number higher,
# like this: range(1, 6).
# If you omit the first number in the range() function, Python automatically starts your count at 0,
# like this: range(6). This is equivalent to range(0, 6), which tells Python to count from 0 to 5.
# The range() function makes it easy to generate a series of numbers.
# For example, to print the numbers from 0 to 5, you could use the following code:
for value in range(6):
    print(value)
# The range() function can take a third argument, which is the amount by which the
# count should increase. By default, the range() function increases the number by 1,
# but if you provide a third value, the range will increase by that amount:
for value in range(1, 10, 2):
    print(value)
# This code tells Python to count from 1 to 9, and increase the value by 2 each time.

# USING range() TO MAKE A LIST OF NUMBERS
# You can use the list() function to quickly generate a list of numbers.
numbers = list(range(1, 6))
print(numbers)

# We can use the range() function to skip numbers. For example, the following code
# makes a list of the odd numbers from 1 to 20:
odd_numbers = list(range(1, 20, 2))
print(odd_numbers)

# Here’s how to make a list of the first 10 square numbers (that is, the
# result of each integer multiplied by itself):

squares = []
for value in range(1, 11):
    square = value*value  # or value**2
    squares.append(square)
print(squares)

# To make your program more concise, you can skip the temporary variable
# square and append each new value directly to the list:
squares = []
for value in range(1, 11):
    squares.append(value**2)
print(squares)

# SIMPLE STATISTICS WITH A LIST OF NUMBERS
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(min(digits))  # minimum value in the list
print(max(digits))  # maximum value in the list
print(sum(digits))  # sum of all values in the list

# LIST COMPREHENSIONS
# the squares example can be rewritten using a list comprehension:

squares = [value**2 for value in range(1, 11)]
# This single line of code does the same work as the four lines we used earlier to generate the list of squares.
print(squares)

# EXERCISES

counting_to_twenty = list(range(1, 21))
print(counting_to_twenty)

millions = list(range(1, 1_000_001))
for million in millions:
    print(million)
print("I am the one in millions!")

millions = list(range(1, 1_000_001))
print(min(millions))
print(max(millions))
print(sum(millions))

odd_numbers = list(range(1, 21, 2))
print(odd_numbers)

threes = []
for three in range(3, 31, 3):
    threes.append(three)
    print(three)
print(threes)

cubes = []
for value in range(1, 11):
    cubes = value**3
    cubes.append(cubes)
print(cubes)

cubes = [value**3 for value in range(1, 11)]

# WORKING WITH LISTS

# slicing a list
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])  # slicing first three players
print(players[1:4])  # slicing from index 1 to index 3
print(players[:4])   # slicing from start to index 3
print(players[2:])   # slicing from index 2 to end
print(players[-3:])  # slicing last three players

# looping through a slice
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())

# COPYING A LIST
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]  # copying the entire

print("My favorite foods are:")
print(my_foods)
print("\nMy friend's favorite foods are:")
print(friend_foods)

my_foods.append('cannoli')
friend_foods.append('ice cream')
print("\nMy favorite foods are:")
print(my_foods)
print("\nMy friend's favorite foods are:")
print(friend_foods)

# EXERCISES WITH SLICING AND COPYING LISTS

precious_metals = ['gold', 'silver', 'platinum', 'diamond', 'ruby', 'emerald']
# first three metals
print(f"The first three items in the list are: {precious_metals[:3]}")
# middle three metals
print(
    f"The first three items in the middle of the list are: {precious_metals[2:5]}")
# last three metals
print(f"The last three items in the list are: {precious_metals[-3:]}")

# _________________
pizzas2 = ['pepperoni', 'mushrooms', 'all the meats']
friend_pizzas = pizzas2[:]  # copying the list of pizzas at line 28
pizzas2.append("veggie")
friend_pizzas.append("hawaiian")
print("My favorite pizzas are:")
for pizza in pizzas2:
    print(pizza)
print("\nMy friend's favorite pizzas are:")
for pizza in friend_pizzas:
    print(pizza)
