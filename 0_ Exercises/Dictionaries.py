# Try it yourself_1

# Person

paola = {
    'first_name': 'Paola',
    'Last_name': 'Flores',
    'favorite_food': 'makis',
    'city': 'Lima'
}

print(paola['first_name'])
print(paola['Last_name'])
print(paola['favorite_food'])

# favorite Numbers

favorite_numbers = {
    'Jose': 69,
    'Ariana': 88,
    'Paola': 2,
    'Jomar': 33,
    'Pedro': 666,
}
print(f"Jose's favorite number is:{favorite_numbers['Jose']}")
print(f"Ariana's favorite numbers is: {favorite_numbers['Ariana']}")

# glossary

glossary = {
    'dictionary': 'An object that allows us to store pieces of related information',
    'get()': 'A method to obtain the value from a key in a dictionary',
    'list': 'An object that allows us to store sets of information in one place',
    'sort': 'A method used to change the order from a list permanently',
    'variable': 'a piece of memory where a value is stored',
}

# print(f"dictionary: \n\t {glossary['dictionary']}.")

# glossary_2

for word, definition in glossary.items():
    word = word.title()
    print(f"{word}:\n\t{definition}.")

# rivers

rivers = {'nile': 'egypt', 'Amazon': 'brazil,peru,bolivia,ecuador,venezuela and guyana',
          'mississippi': 'United States'}

for river, country in rivers.items():
    print(f"The {river.title()} runs through {country.title()}.")
print("\n")
for river in rivers:

    print(river.title())
print("\n")
for country in rivers.values():

    print(country.title())
