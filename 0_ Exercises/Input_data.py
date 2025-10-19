"""Input data handling functions.
- input(): Reads a line of text from the user.
- int(): Converts a value to an integer.
- float(): Converts a value to a floating-point number.
- str(): Converts a value to a string.
- bool(): Converts a value to a boolean (True or False).
- eval(): Evaluates a string as a Python expression (use with caution).
- type(): Returns the type of a value.
"""
x = input("Enter Value of x: ")
y = int(x) + 1
print(f"x:{x}, y:{y}")  # x is string, y is integer
print(type(x), type(y))  # <class 'str'> <class 'int'>
