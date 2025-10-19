"""This module demonstrates variable declarations and initializations in Python.
It includes the following rules for variable names:
1. Variable names must start with a letter (a-z, A-Z) or an underscore (_).
2. Variable names can contain letters, digits (0-9), and underscores (_).
3. Always use lowercase letters for variable names.
4. Variable names cannot be a reserved keyword in Python.
5. Variable names should be descriptive and meaningful.
6. Use underscores to separate words in variable names (snake_case).
7. Avoid using special characters or spaces in variable names.
8. Variable names are case-sensitive.
9. Do not start variable names with a digit.
10. Avoid using single-character variable names except for counters or iterators.
11. Use plural names for variables that hold collections of items (e.g., students, items).
12. Use singular names for variables that hold a single item (e.g., student, item).
13. Avoid using names that are too similar to built-in functions or types (e.g., list, str).
14. Keep variable names concise but informative.
15. Use consistent naming conventions throughout your code.
16. Avoid using abbreviations unless they are widely understood.
"""

students_count = 1000
rating = 4.99
is_published = True
course_name = "Python Programming"

# strings

name = 'John Doe'
address = "123 Main St, Anytown, USA"

# String indexing and slicing examples

print(name[0])  # Output: 'J'
print(name[1:4])  # Output: 'ohn'

# Output: 'Jh o' This is an example of string slicing in Python, which uses the syntax [start:stop:step].
print(name[0:8:2])


print(name[-1])  # Output: 'e'
print(name[0:])  # Output: 'John Doe'
print(name[:4])  # Output: 'John'
print(name[:])  # Output: 'John Doe'

# formatted strings(f-strings)
# In some situations, you’ll want to use a variable’s value inside a string. For
# example, you might want to use two variables to represent a first name and a
# last name, respectively, and then combine those values to display someone’s
# full name:

first = "John"
last = "Doe"
full_name = first + " " + last
print(full_name)  # Output: John Doe - concatenation

full_name = f"{first} {last}"
print(full_name)  # Output: John Doe

first_name = "Ada"
last_name = "Lovelace"
full_name = f"{first_name} {last_name}"
print(f"Hello, {full_name.upper()}!")   # Output: Hello, Ada Lovelace

# This module demonstrates escape sequences
# To include special characters in strings that are otherwise difficult to type directly.

# \n - New Line
# \t - Tab
# \r - Carriage Return
# \' - Single Quote
# \" - Double Quote
# \b - Backspace
# \f - Form Feed
# \v - Vertical Tab
# \\ - Backslash


course_name = "Python's Course for \nBeginners"
print(course_name)  # Output: Python's Course for Beginner
course_name = "\tPython"
print(course_name)  # Output:     Python
course_name = "Python\\Course"
print(course_name)  # Output: Python\Course
course_name = "Python\fCourse"
print(course_name)  # Output: PythonCourse
course_name = "Python\bCourse"
print(course_name)  # Output: PythonCourse
course_name = "Python\rCourse"
print(course_name)  # Output: Course
course_name = "Python\vCourse"
print(course_name)  # Output: PythonCourse (Vertical Tab)

print("Languages:\n\tPython\n\tC\n\tJavaScript")


# String Methods:

# Python provides several built-in string methods that allow you to manipulate and work with strings effectively. Here are some commonly used string methods:

# 1. lower(: Converts all characters in the string to lowercase.
# 2. upper(): Converts all characters in the string to uppercase.
# 3. title(): Converts the first character of each word to uppercase and the rest to lowercase.
# 4. strip(): Removes leading and trailing whitespace from the string.
# 5.find(substring): Returns the lowest index of the substring if found in the string. Returns -1 if not found.
# 6.replace(old, new): Replaces all occurrences of the old substring with the new substring.
# 7.in operator: Checks if a substring exists within the string and returns True or False.


course = "Python for Beginners"

print(course.lower())  # Output: python for beginners
print(course.upper())  # Output: PYTHON FOR BEGINNERS
print(course.title())  # Output: Python For Beginner
                    

ce
course="   Python for Beginners   "
print(course.strip())  # Output: Python for Beginners
  
# Finding Substrings
print(course.find("for"))  # Output: 7
print("Python" in course)  # Output: True
print("Java" in course)  # Output: False
print("Java" not in course)  # Output: True
print("Python" not in course)  # Output: False

# Replacing Substrings in a String

print(course.replace("Beginners", "Absolute Beginners")) # Output: Python for Absolute Beginners # Original string remains unchanged: Python for Beginners
print(course.replace("for", "4"))  # Output: Python 4 Beginners
# Output: Python for riginal string remains unchangedBeginners
print(course.replace("Beginners", ""))
print(course.replace("for", "4")) utput4

# Removingl="https://nostarch.com" 
nostarch_url=nostarch_url.removeprefix("https://") 
print(nostar c h_url)  # Output: nostrch.com 
nostarch_url = nostarch_url.removesuffix(".com") 
print(nostarch_url)  # Output: nostarch 
  
#EXERCISES 

# ame="Paol

name t (name)

name = name.upper()
print(name)

name = name.lower()
print(name)

name = name.title()
print(name)

name = name.strip()
print(name)


quote='Albert Einstein once said, "A person who never made a mistake never tried anything new"'
print(quote)
  
quote2= 'Price is what you pay. Value is what you get.'
message= f'Warren Buffet once said, "{quote2}"'
print( message) 
 
filename='pyth

filename  

