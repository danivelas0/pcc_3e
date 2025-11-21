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
restaurant.increment_number_served (100)
restaurant.show_number_served()
