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

# GLOSSARY_2

for word, definition in glossary.items():
    word = word.title()
    print(f"{word}:\n\t{definition}.")

# RIVERS

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

# POLLING
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
}

poll_names = ['jen', 'sarah', 'edward', 'phil', 'thomas', 'peter', 'jorge']

for poll_name in poll_names:
    if poll_name in favorite_languages.keys():
        print(f'Than you for taking the Poll {poll_name}!')
    else:
        print(f'You must take the poll {poll_name}!')

# 6.7 People:

people = []

# make new user

person = {
    'first_name': 'paola',
    'Last_name': 'flores',
    'favorite_food': 'makis',
    'city': 'Grecia',
    'pet': 'tom'
}
# add new user to list
people.append(person)

# make new user
person = {
    'first_name': 'elisa',
    'Last_name': 'larez',
    'favorite_food': 'chorizo',
    'city': 'roma',
    'pet': 'pancho',
}
# add new user to list
people.append(person)

# print users info

print('People information:\n')
for person in people:
    print(f"{person['first_name'].title()} information is:\n\t")
    for prop, description in person.items():
        print(f'\t{prop}: {description}')
    print('\n')

# pets

pets = []

pet = {
    'specie': 'cat',
    'name': 'juliana',
    'color': 'orange',
    'food': 'meat',
    'owner': 'jose',
}

pets.append(pet)

pet = {
    'specie': 'dog',
    'name': 'tobias',
    'color': 'champagne',
    'food': 'chicken',
    'owner': 'ariana',
}

pets.append(pet)

for pet in pets:
    print(f'Pet Information:\n')
    for prop, description in pet.items():
        print(f'{prop}: {description}')
    print('\n')

# cities

cities = {
    'roma': {
        'country': 'Italy',
        'population': '2.8 millions',
        'fact': 'Vatican city',
    },
    'paris': {
        'country': 'France',
        'population': '2.1 millions',
        'fact': 'for 200 years, it was technically illegal for women to wear trousers'
    },
}

for city, city_info in cities.items():
    print(f'{city.title()} information is:\n')
    print(f"\tCountry: {city_info['country']}")
    print(f"\tPopulation: {city_info['population']}")
    print(f"\tFact: {city_info['fact']}")
    print('---')
