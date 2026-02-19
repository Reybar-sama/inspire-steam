# Name : Rey Bar
# Date : 19/02/2026
# Classes (Objects) in Python

class Human:
    # human attributes
    type = "mammal"
    legs = 2
    brain = True
    warm_blooded = True
    city = "Nairobi"

    # constructor for class object
    # constructor will be used to create copies of 
    def __init__(self, name, age):
        self.human_name = name
        self.human_age = age 

    def tell_story(self):
        print(f"Hello, I'm {self.human_name}. Here is a story:")
        print("Mnabeba ligi ama tuanze kuwatafutia bottles za kuwekea machozi? The Arsenal ehhh??")

# create objects
armani = Human("Armani", 69,)
thomas_frank = Human("Thomas Frank", 41)

# Let the human created do tings
armani.tell_story()
print("Armani's age is:", armani.human_age)

# modify one of the objects without modifying other objects
thomas_frank.city = "London"

print("Thomas Frank's location:", thomas_frank.city)
print("Armani's location:", armani.city)


