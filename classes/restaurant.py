class Restaurant:
    """A class representing a restaurant"""

    def __init__(self, name, cuisine):
        """Initialize name and cuisine attributes"""

        self.name = name.title()
        self.cuisine = cuisine.title()
        self.number_served = 0

    def describe_restaurant(self):
        """Display a summary of the restaurant"""
        msg = f"{self.name} serves wonderful {self.cuisine} food, it has served {self.number_served}."
        print(f"\n{msg}")

    def open_restaurant(self):
        """Display a message that the restaurant is open"""
        msg = f"{self.name} is open, come on in." 
        print(f"\n{msg}")
    
    def set_number_served(self, number_served):
        self.number_served = number_served

    def increment_number_served(self, additional_served):
        self.number_served += additional_served

class IceCreamStand(Restaurant):
    
    def __init__(self, name, cuisine='Ice Cream'):
        super().__init__(name, cuisine)
        self.flavors = []

    def display_flavors(self):
        """Display the ice cream flavors"""
        
        print(f"Ice cream flavors available:")
        for flavor in self.flavors:
            print(f"- {flavor}")
    
restaurant = Restaurant('Bob', 'goofy')
restaurant.set_number_served(24)
restaurant.increment_number_served(12)

print(restaurant.name)
print(restaurant.cuisine)

restaurant.describe_restaurant()
restaurant.open_restaurant()

small_one = IceCreamStand('Dingle')
small_one.flavors = ['vanilla', 'chocolate', 'strawberry', 'redbull', 'orange']
small_one.describe_restaurant()
small_one.display_flavors()
