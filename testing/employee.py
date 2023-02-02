class Employee():

    def __init__(self, first_name, last_name, annual_salary) -> None:
        """Initializing attributes"""

        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.annual_salary = annual_salary 

    def give_raise(self, bonus=5000):
        self.annual_salary += bonus

