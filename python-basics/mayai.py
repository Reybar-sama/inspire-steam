# Name : Rey Bar
# Date : 19/02/2026
# (s)eggs

def cook_egg():
    pan = True
    moto = True
    eggs = 4
    oil = 20 

    print(f"The pan is {pan}, the fire is {moto},\
            add {oil} ml of oil and cook {eggs} eggs.")

    print("Here is statement 1")

    print("Here is statement 2")

    cook_egg()

    print("Here is statement 3")

# Ride fare creating function

def create_fare(route, distance, rush_hour):

    fare = distance * 10
    if rush_hour == True:
        fare = fare * 1.5
    print(f"Your fare to {route} is {fare}.")

    return fare 

rush_hour_cost = True
returned_fare = create_fare("Juja-Allsops", 7, rush_hour_cost)
print(f"The fare returned is: {returned_fare}")

# Passing a list as a parameter
def write_all_interests(interests):
    for interest in interests:
        print(f"I am interested in {interest}")

all_interests = ["Riding", "Repairing", "Role-playing", "Formula 1"]

write_all_interests(all_interests)


