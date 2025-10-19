"""Numbers' module

This module demonstrates the use of numbers in Python, including integers and floating-point numbers.
It also covers basic arithmetic operations and type conversion.

Python supports two main types of numbers:
1. Integers (int): Whole numbers without a decimal point, e.g., 1, -5, 1000.
2. Floating-point numbers (float): Numbers with a decimal point, e.g., 3.14, -0.001, 2.0.
3. Complex numbers (complex): Numbers with a real and imaginary part, e.g., 2 + 3j.

Common arithmetic operations:
- Addition (+)
- Subtraction (-)
- Multiplication (*)
- Division (/)
- Floor Division (//)
- Modulus (%)
- Exponentiation (**)
- Parentheses for grouping (())
- Augmentation operators (+=, -=, *=, /=, //=, %=, **=)
"""

import math  # Importing the math module for additional mathematical functions
import this  # The Zen of Python, by Tim Peters

# Basic arithmetic operations

x = 10 + 5   # Addition
y = 10 - 5   # Subtraction
z = 10 * 5   # Multiplication
a = 10 / 5   # Division floating point
b = 10 // 3  # Floor Division integer
c = 10 % 3   # Modulus - remainder of division
d = 10 ** 3  # Exponentiation - power
e = (10 + 3) * 2  # Parentheses for grouping

x += 3  # x = x + 3
y -= 3  # y = y - 3
z *= 3  # z = z * 3
a /= 3  # a = a / 3
b //= 3  # b = b // 3
c %= 3  # c = c % 3
d **= 3  # d = d ** 3
print(x, y, z, a, b, c, d, e)

# Python defaults to a float in any operation that uses a float, even if the
# output is a whole number.

x = 5/2  # Output: 2.5 (float)
y = 5.0/2  # Output: 2.5 (float)
z = 5//2  # Output: 2 (int)
a = 5.0//2  # Output: 2.0 (float)
b = 5*2.0  # Output: 10.0 (float)
c = 5*2  # Output: 10 (int)
print(x, y, z, a, b, c)

# Underscores in numeric literals
# You can use underscores to make large numbers more readable:

population = 1_000_000  # 1 million
print(population)
universe_age = 14_000_000_000  # 14 billion
print(universe_age)
distance_to_sun = 93_000_000  # 93 million miles
print(distance_to_sun)

# constants
# Python does not have built-in constant types, but by convention, variables
# that are meant to be constants are written in uppercase letters.

PI = 3.14159
SPEED_OF_LIGHT = 299_792_458  # in meters per second
GRAVITATIONAL_CONSTANT = 6.67430e-11  # in m^3 kg^-1 s^-2

# MATH FUNCTIONS

# Python provides several built-in functions to perform mathematical operations on numbers:

# - abs(): Returns the absolute value of a number.
# - round(): Rounds a floating-point number to the nearest integer or to a specified number of decimal places.
# - pow(): Raises a number to the power of another number.
# - min(): Returns the smallest of the input values.
# - max(): Returns the largest of the input values.

# - int(): Converts a value to an integer.
# - float(): Converts a value to a floating-point number.
# - complex(): Converts a value to a complex number.
# -bool(): Converts a value to a boolean(True or False).
# -str(): Converts a value to a string.

# MATH MODULE

# The math module provides additional mathematical functions and constants:

# - math.sqrt(): Returns the square root of a number.
# - math.ceil(): Rounds a number up to the nearest integer.
# - math.floor(): Rounds a number down to the nearest integer.
# - math.factorial(): Returns the factorial of a number.
# - math.pi: The mathematical constant π(approximately 3.14159).


x = -5
print(abs(x))          # Output: 5
print(round(3.14))     # Output: 3
print(round(3.14159, 2))  # Output: 3.14
print(pow(2, 3))      # Output: 8
print(min(1, 2, 3))   # Output: 1
print(max(1, 2, 3))   # Output: 3

print(math.sqrt(16))    # Output: 4.0
print(math.ceil(3.14))  # Output: 4
print(math.floor(3.14))  # Output: 3
print(math.factorial(5))  # Output: 120
print(math.pi)          # Output: 3.141592653589793

# type conversion

print(float(5))        # Output: 5.0
print(int(3.99))      # Output: 3
print(complex(2, 3))  # Output: (2+3j)
