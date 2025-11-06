# EXERCISES

# 8-1 MESSAGE:

def display_message():
    print('Hi everyone, I\'m learning about python functions.')


display_message()

# 8-2 FAVORITE BOOK:


def favorite_book(title):
    print(f'One of my favorite books is:{title}!')


favorite_book('The subtle art of not giving a fuck')

# T-Shirt


def make_shirt(shirt_size, shirt_message):
    print(f"Shirt size: {shirt_size},\nShirt message: {shirt_message}")


make_shirt('M', 'I am the best!')
make_shirt(shirt_size='medium', shirt_message='I love Python')

# 8-4 Large_shirts_default


def make_shirt(shirt_message='I Love Python', shirt_size='large'):
    print(f"Shirt size: {shirt_size},\nShirt message: {shirt_message}")


make_shirt()
make_shirt(shirt_size='medium')
make_shirt(shirt_message='I AM THE BEST', shirt_size='Extra Large')

# 8-5 Cities


def describe_city(city_name, country='Brazil'):
    print(f"{city_name} is in {country}")


describe_city('Rio di Janeiro')
