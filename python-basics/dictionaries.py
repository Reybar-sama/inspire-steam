# Name : Rey Bar
# Date : 18/02/2026
# Program to show dictionaries in Python

cars = {"Make": "Porsche" , 
        "Model": "918 Spyder",
        "Color": "Magno Blue", 
        "Year":  "2013"}

print(cars)

print(cars["Model"])
print(cars["Year"])

students = {"Alice": 24, 
                "May": 18,  
                "Mark": 22, 
                "Daisy": 19}
for key in students:
    print(key)

for val in students.values():
    print(val)