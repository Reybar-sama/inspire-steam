# Name : Rey Bar
# Date : 13/02/2026
# Table of squares

numbers = [1,2,3,4,5,6,7,8,9,10]
squares =  [x**2 for x in numbers]

print(squares)

for x in range (0,21):
    print(x**2)

from tabulate import tabulate

data = [
    [numbers, squares]
]

headers = ["Number", "Square of number"]

print(tabulate(data, headers=headers, tablefmt="grid"))


