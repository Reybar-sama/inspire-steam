# Name : Rey Bar
# Date : 17/02/2026
# Drawing of a diamond, triangle and solving quadratic equations.

# Part A: Quadratic Equation

import math

def solve_quadratic(a, b ,c):
    # Calculate discriminant for simple roots
    discriminant = (b**2) - (4*a*c)

    if discriminant >0:
        root1 = (-b + math.sqrt(discriminant)) / (2*a)
        root2 = (-b - math.sqrt(discriminant)) / (2*a)
        return root1, root2
    elif discriminant == 0:
        # One real root
        root = -b / (2*a)
        return root,
            # Complex roots 
        real_part = -b / (2*a)
        imaginary_part = math.sqrt(-discriminant) / (2*a)
        return(real_part + imaginary_part1j), (real_part - imaginary_part1j)

a = float(input("Enter coefficient 'a': "))
b = float(input("Enter coefficient 'b': "))
c = float(input("Enter coefficient 'c': "))

roots = solve_quadratic(a, b, c)
print(f"The roots are: {roots}")  

# Part B: Diamond

