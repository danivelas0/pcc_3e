# TUPLES
# List of items that cannot be changed (immutable)
# Created using parentheses ()

# DEFINING A TUPLE
dimensions = (200, 100)

my_tuple = (1,)  # single item tuple needs a comma at the end

# Looping Through All Values in a Tuple
dimensions = (200, 100)
for dimension in dimensions:
    print(dimension)

# MODIFYING A TUPLE
# Tuples are immutable, but you can reassign a variable to a new tuple
dimensions = (200, 100)
print("Original dimensions:")
for dimension in dimensions:
    print(dimension)
dimensions = (400, 200)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)

# TRY IT YOURSELF
# 1. Create a tuple named foods with your favorite foods
foods = ('pizza', 'sushi', 'tacos', 'pasta', 'ice cream')
print("My favorite foods are:")
for food in foods:
    print(food)
print("\nModified favorite foods:")
# 2. Try to modify the tuple (this will raise an error)
# foods[0] = 'burger'  # Uncommenting this line will raise a TypeError
# 3. Reassign the variable foods to a new tuple with different foods
foods = ('burger', 'salad', 'steak', 'fries', 'cake')
for food in foods:
    print(food)
