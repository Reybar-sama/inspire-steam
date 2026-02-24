# Name : Rey Bar
# Date : 24/02/2026
# Program to perform file operations.

# create new file
new_file = open("king_kunta.txt", "a")

# write to new file
new_file.write("\nStudent Name : Big Smoke\n,\nID : 67694207\n, \nemail: smokebig@gmail.com\n")



# read from the file
new_file = open("king_kunta.txt", "r")
data = new_file.read()

print(data)
# delete file
import os
os.remove("remontada.txt")

# delete folder
os.rmdir()
# us os remove
