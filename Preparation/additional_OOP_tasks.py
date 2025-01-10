# abstraction
from abc import ABC


class Car(ABC):
    def __init__(self, brand, model,year):
        self.brand = brand
        self.model = model
        self. year = year

    def printDetails(self):
        pass

    def accelerate(self):
        print("Speed up ...")

    def break_applied(self):
        print("Car stopped")


class Hatchback(Car):
    def printDetails(self):
        print("Brand:", self.brand)
        print("Model:", self.model)
        print("Year:", self.year)

    def sunroof(self):
        print("Not having this feature")


# Create a child class
class Suv(Car):
    def printDetails(self):
        print("Brand:", self.brand)
        print("Model:", self.model)
        print("Year:", self.year)

    def sunroof(self):
        print("Available")


class Main :
    def main(self):
        # Create an instance of the Hatchback class
        car1 = Hatchback("Maruti", "Alto", "2022")

        # Call methods
        car1.printDetails()
        car1.accelerate()
        car1.sunroof()
#inheritance
#encapsulations
# polymorhism