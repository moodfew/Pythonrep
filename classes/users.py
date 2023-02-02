class User:
    """A class representing an user"""

    def __init__(self, first_name, last_name, username, email, phone_number):
        """Initializing the attributes"""

        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.username = username
        self.email = email
        self.phone_number = phone_number
        self.login_attempts = 0
    
    def describe_user(self):
        """Display a summary about the user"""
        print(f"\n{self.first_name} {self.last_name}")
        print(f"  Username: {self.username}")
        print(f"  Email: {self.email}")
        print(f"  Phone number: {self.phone_number}")

    def greet_user(self):
        """Display a personalized greeting for user"""
        print(f"\nWelcome back, {self.username}")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0
        

class Admin(User):
    """A child class representing a special user called Admin"""
    def __init__(self, first_name, last_name, username, email, phone_number):
        super().__init__(first_name, last_name, username, email, phone_number)

        # Initialize an empty set of privileges.
        self.privileges = Privileges()

class Privileges():
    """A class to store admin's privileges"""
    def __init__(self, privileges=[]) -> None:
        self.privileges = privileges

    def show_priviliges(self):

     """Displaying Admin's privileges"""
     print(f"\nAdmin  privileges:")
     if self.privileges:
         for privilege in self.privileges:
             print(f"- {privilege}")

     else:
         print("This user does not has no privileges.")


        


admin1 = Admin('Kumala', 'Savesta', 'kumalasolos', 'kumaladingles@goofyah.com', '82193132')
admin1.describe_user()

admin1.privileges.privileges = ['can delete users',
                     'can add users',
                     'can install or remove software',
                     'can make modifications to the server']

admin1.privileges.show_priviliges()



bob = User('bob', 'dob', 'goofyah', 'akldjlaj@gmail.com', '213131231311312')
bob.describe_user()
bob.greet_user()
       
bob.increment_login_attempts()
bob.increment_login_attempts()
bob.increment_login_attempts()
bob.increment_login_attempts()
bob.increment_login_attempts()
bob.increment_login_attempts()

print("\nIncremented attempts:")
print(bob.login_attempts)

bob.reset_login_attempts()
print("Resetted login attempts")
print(bob.login_attempts)
