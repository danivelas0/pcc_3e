class Restaurant:
    """ A class for a Restaurant """

    def __init__(self, name, cuisine_type):
        self.name = name.title()
        self.cuisine_type = cuisine_type
        self.numbers_served = 0

    def describe_restaurant(self):
        """Describes the restaurant attributes"""
        print(f'Restaurant name is: {self.name}')
        print(f'The cousine type is: {self.cuisine_type}')

    def open_restaurant(self):
        """Indicates wether the restaurant is open """
        print(f"The restaurant {self.name} is open")

    def set_number_served(self, numbers_served):
        '''Sets the number of customers served'''
        if self.numbers_served >= 0:
            self.numbers_served = numbers_served
        else:
            print('You can\'t set negative numbers')

    def increment_number_served(self, number):
        '''Updates and increments the number of customers served'''
        if self.numbers_served >= number:
            self.numbers_served += number
        else:
            print('You can\'t roll back the number of customers served')

    def show_number_served(self):
        '''Prints the number of customers served in a business day'''
        print(f'Today, {self.numbers_served} customers were served.')


restaurant = Restaurant('Maido', 'Japanese Cuisine')
restaurant.describe_restaurant()
restaurant.set_number_served(100)
restaurant.show_number_served()
restaurant.increment_number_served(100)
restaurant.show_number_served()


class User:
    """Information about User"""

    def __init__(self, first_name, last_name, location, age):
        self.first_name = first_name
        self.last_name = last_name
        self.location = location
        self.age = age
        self.login_attempts = 0

    def describe_user(self):
        """Describes the User"""
        print(f'User\'s name:{self.first_name} {self.last_name}')
        print(f'User\'s location:{self.location}')
        print(f'User\'s age:{self.age} years old')

    def greet_user(self):
        print(f'Hello {self.first_name}, you are very Welcome!')

    def increment_login_attempts(self, login_attempt):
        '''Increments the amount of login attempts'''
        login_attempts += login_attempt

    def reset_login_attempts(self):
        '''Resets login attempts'''
        self.login_attempts = 0


user_1 = User('Daniel', 'Velasquez', 'Peru', '33')
user_2 = User('John', 'Zena', 'Australia', '24')
user_3 = User('Maria', 'Ramirez', 'Argentina', 50)

user_1.describe_user()
user_2.describe_user()
user_3.describe_user()

user_1.greet_user()

# INHERITANCE
