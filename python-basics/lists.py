# Name : Rey Bar
# Date : 18/02/2026
# Program to show lists in Python
# list of friends
friends = ["Rachel", "Phoebe", "Ross", "Chandler","Monica","Joey"]

print(friends)
friends.sort()
print(friends)

friends.reverse()
print(friends)
friends.append("Jack")
print(friends)

new_friends = ["Kubica", "Schumacher", "Senna", "Alonso", "Maldonaldo"]

print(len(new_friends))

# new list of friends
students = friends + new_friends

print(students)
students.pop()
print(students)
students.insert(5, "Hamilton")
print(students)
students.extend('Mazespin')
print(students)

students.remove("Alonso")
print(students)

new_students = students.copy()
print(new_students)