# Name : Rey Bar
# Date : 17/02/2026
# Program to format output in di

name = "Rey Bar" # name

weight = 75 # weight in kgs

fav_team = "Chelsea Football Club"

height = 176 # height in centimetres

# 1. format using printf(f"{}")

print(f"My name is {name} and I weigh {weight} kgs.")

# 2. using f-string
msg = f"My name is {name} and I support {fav_team}."
print(msg)

# 3. using {} and .format()

print("My name {0} and I am {1} cm tall." .format(name, height))

# using output specifies %s(strings) and %f(float)

import math
print(f"The value of pi is approximately %5.3f." % math.pi)
print(f"I support %s " % fav_team)