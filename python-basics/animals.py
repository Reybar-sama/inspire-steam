# Name : Rey Bar
# Date : 23/02/2026
# Program to show inheritance in Python

class Animal():
    def __init__(self, species, weight, food):
        self.species = species
        self.weight = weight
        self.food = food

    def grow(self, weight):
        weight = 1.1 * weight
        print(f"The animal weighs {weight} kgs.")

    def eat(self, food):
        print(f"The animal eats {food}")

class Dog(Animal):

    def __init__(self, color, height, breed):
        super().__init__(species, weight, food)
        self.color = color
        self.height = height
        self.breed = breed

    def barks(self):
        print(f"The dog")

class Horse(Animal):