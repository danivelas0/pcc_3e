"""LITS MODULE 
Lists are a built-in data type in Python that can store multiple items in a single variable.They are ordered, changeable, and allow duplicate values.

Lists are defined by enclosing items in square brackets [] and separating them with commas.

This module contains functions that demonstrate various operations on lists in Python.

It includes functions to create, modify, and manipulate lists, as well as perform common list operations.

Each function includes a brief description of its purpose and usage.
"""

bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)
print(bicycles[0])  # Accessing the first element of the list
# Accessing and modifying the first element of the list
print(bicycles[0].title())
print(bicycles[1])
print(bicycles[3])

message = f"My first bicycle was a {bicycles[0].title()}"
print(message)

# Exercises

Names = ["Paola", "Ariana", "Jose", "Jomar", "Pedro"]
print(Names[0])
print(Names[1])
print(Names[2])
print(Names[3])
print(Names[4])

message = f"Hello {Names[0]}, how are you?"
print(message)
message = f"Hello {Names[1]}, how are you?"
print(message)
message = f"Hello {Names[2]}, how are you?"
print(message)
message = f"Hello {Names[3]}, how are you?"
print(message)
message = f"Hello {Names[4]}, how are you?"
print(message)

# Modifying elements in a list

# Most lists you create will be dynamic, meaning you’ll build a list and then
# add and remove elements from it as your program runs its course.

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles[0] = 'ducati'  # Changing the first element of the list
print(motorcycles)

# ADDING ELEMENTS TO A LIST

# When you append an item to a list, the new element is added to the end
# of the list.

motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.append('harley-davidson')
motorcycles.append("ducati")
print(motorcycles)

# The append method makes it easy to build lists dynamically. For
# example, you can start with an empty list and then add items to the list using
# a series of append calls

fruits = []
fruits.append("apple")
fruits.append("banana")
fruits.append("cherry")
print(fruits)

# INSERTING ELEMENTS INTO A LIST

# You can insert a new element at any position in a list by using the insert()

cities = ['New York', 'Los Angeles', 'Chicago']
cities.insert(1, 'Houston')  # Inserting 'Houston' at index 1
print(cities)

# REMOVING ELEMENTS FROM A LIST

# if you know the position of the item you want to remove from a list, you can
# use the del statement. For example, the following code removes the first item in

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
del motorcycles[0]
print(motorcycles)

# The del statement removes the item at the specified index, but it does not
# return the value of the removed item.

# If you want to work with a value that
# you are removing from a list, you can use the pop() method. The pop() method
# removes the last item in a list, but it lets you work with that item after it
# has been removed.

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

popped_motorcycle = motorcycles.pop()
print(popped_motorcycle)

last_owned = motorcycles.pop()
print(f"The last motorcycle I owned was a {last_owned.title()}.")

# You can also pop items from any position in a list by
# including the index of the item you want to remove in parentheses

motorcycles = ['honda', 'yamaha', 'suzuki']
first_owned = motorcycles.pop(0)  # popping the first item
print(f"The first motorcycle I owned was a {first_owned.title()}.")

# Remember that each time you use pop(), the item you work with is no
# longer stored in the list.

# If you’re unsure whether to use the del statement or the pop() method,
# here’s a simple way to decide: when you want to delete an item from a list
# and not use that item in any way, use the del statement; if you want to use an
# item as you remove it, use the pop() method.

# Removing an item by value

# Sometimes you won’t know the position of the value you want to remove from
# a list. If you only know the value of the item you want to remove, you can
# use the remove() method.

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)
motorcycles.remove('ducati')  # Removing 'ducati' by value
print(motorcycles)

too_expensive = 'ducati'  # Removing 'ducati' by value stored in a variable
print(f"\nA {too_expensive.title()} is too expensive for me.")

# The remove() method deletes only the first occurrence of the value you
# specify. If there’s a possibility the value appears more than once in the
# list, you’ll need to use a loop to make sure all occurrences of the value
# are removed.

# EXERCISES

guest_list = ["Charlie Munger", "Isaac Newton", "Nikola Tesla"]

print(f"Dear {guest_list[0]}, you are invited to dinner.")
print(f"Dear {guest_list[1]}, you are invited to dinner.")
print(f"Dear {guest_list[2]}, you are invited to dinner.")
print(f"\n{guest_list[2]} can't make it to the dinner.")

new_guest = "Albert Einstein"
guest_list[2] = new_guest
print(f"\nDear {guest_list[0]}, you are invited to dinner.")
print(f"Dear {guest_list[1]}, you are invited to dinner.")
print(f"Dear {guest_list[2]}, you are invited to dinner.")

print("\nGood news, we found a bigger dinner table!\n")

guest_list.insert(0, "Warren Buffett")
guest_list.insert(2, "Alexander The Great")
guest_list.append("Monish Pabrai")
print(f"\nDear {guest_list[0]}, you are invited to dinner.")
print(f"Dear {guest_list[1]}, you are invited to dinner.")
print(f"Dear {guest_list[2]}, you are invited to dinner.")
print(f"Dear {guest_list[3]}, you are invited to dinner.")
print(f"Dear {guest_list[4]}, you are invited to dinner.")
print(f"Dear {guest_list[5]}, you are invited to dinner.")

print("\nUnfortunately, the new dinner table won't arrive on time, and we can only invite two people for dinner.\n")

popped_guest = guest_list.pop()
print(f"Dear {popped_guest}, I'm sorry to inform you that you can't make it to the dinner, because of the new dinner table delay.")
popped_guest = guest_list.pop()
print(f"Dear {popped_guest}, I'm sorry to inform you that you can't make it to the dinner, because of the new dinner table delay.")
popped_guest = guest_list.pop()
print(f"Dear {popped_guest}, I'm sorry to inform you that you can't make it to the dinner, because of the new dinner table delay.")
popped_guest = guest_list.pop()
print(f"Dear {popped_guest}, I'm sorry to inform you that you can't make it to the dinner, because of the new dinner table delay.\n")
print(f"Dear {guest_list[0]}, you are still invited to dinner.")
print(f"Dear {guest_list[1]}, you are still invited to dinner.\n")

del guest_list[0]
del guest_list[0]
print(guest_list)

# ORGANIZING A LIST

# You can easily organize a list by sorting its elements in
# alphabetical order or reverse alphabetical order. You can also sort a list
# numerically, and you can reverse the order of a list no matter how it’s
# currently organized.

# Permanent sorting a list with the sort() method

cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()  # Sorting the list in alphabetical order permanently
print(cars)
# Sorting the list in reverse alphabetical order permanently
cars.sort(reverse=True)
print(cars)

# Temporary sorting a list with the sorted() function
cars = ['bmw', 'audi', 'toyota', 'subaru']
print("Here is the original list:")
print(cars)
print("\nHere is the sorted list:")
print(sorted(cars))  # Temporarily sorting the list in alphabetical order
print("\nHere is the original list again:")
print(cars)
print("\nHere is the sorted list in reverse alphabetical order:")
# Temporarily sorting the list in reverse alphabetical order
print(sorted(cars, reverse=True))
print("\nHere is the original list again:")
print(cars)

# Reversing the order of a list with the reverse() method
# You can reverse the elements of a list in place with the reverse() method.

cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
cars.reverse()  # Reversing the order of the list not in an alphabetical order
print(cars)
# The reverse() method changes the order of a list permanently, but you
# can revert to the original order anytime by applying reverse() to the same
# list a second time.
cars.reverse()
print(cars)

# FINDING THE LENGTH OF A LIST
# You can find the number of items in a list by using the len() function.
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(len(cars))  # Finding the length of  LIST.
# python counts the items in the list starting from 1.

# EXERCISES

# Exercise 3.8 Seeing the World
world_places = ["Switzerland", "Germany", "Maldivas", "Italy", "Greece"]
print("Original list:")
print(world_places)
print("\nSorted list:")
print(sorted(world_places))
print("\nOriginal list again:")
print(world_places)
print("\nReverse list:")
world_places.reverse()
print(world_places)
world_places.reverse()
print("\nOriginal list again:")
print(world_places)
print("\nSort list:")
world_places.sort()
print(world_places)
print("\nReverse sorted list:")
world_places.sort(reverse=True)
print(world_places)
print(f"\nNumber of places in the list: {len(world_places)}")

# EXERCISE 3.9 Dinner Guests
dinner_guests = ["Charlie Munger", "Isaac Newton", "Nikola Tesla"]
print(f"The number of guest is: {len(dinner_guests)}")

# AVOIDING INDEX ERRORS
# An IndexError occurs when you try to access an index that is outside the range of valid indexes for a list.
# For example, if you have a list with three elements and you try to access the fourth element, you will get an IndexError.

motorcycles = ['honda', 'yamaha', 'suzuki']
# This will raise an IndexError because there is no index 3 in the list.
print(motorcycles[3])
