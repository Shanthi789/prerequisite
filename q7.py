class Car:
    """
    Task 1
    - Define a class named Car with attributes: make, model, year
    - Initialize these attributes in the __init__ method
    - Add a method named describe_car() that prints information about the car as "Year Make Model"
    """
    def __init__(self,Make, Model,Year):
        self.make = Make
        self.model = Model
        self.year = Year

    def describe_car(self):
        print("I am a car of make "+self.make+ " , model "+self.model+" ,year "+str(self.year))


# Task 2
# Create an instance of the Car class with the following attributes and call describe_car method:
# - Make: Toyota, Model: Corolla, Year: 2020
car1 = Car('Toyoto', 'Corolla', 2020)
car1.describe_car()
