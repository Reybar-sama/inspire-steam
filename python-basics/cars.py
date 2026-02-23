# Name : Rey Bar
# Date : 11/02/2026
# Program to show classes in Python

class Car():
    # Attributes of car
    def __init__(self, model, make, color, year):
        self.model = model
        self.make = make
        self.color = color
        self.year = year

    # print car details
    def print_details(self, model, make, color, year):
        print(f"{make} {model} of {color} colour was manufactured in the year {year}.")
    
# instantiate class object

my_car = Car("Carrera T", "Porsche", "Purple", "2026")
mzae_car = Car("Vanquish", "Aston Martin", "Black", "2025")

my_car.print_details("Carrera T", "Porsche", "Purple", "2026")
   

