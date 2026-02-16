# Name : Rey Bar
# Date : 16/02/2026
# Program to calculate factorials of numbers

number = int(input("Enter the number x:")) # input from user
factorial = 1 # init factorial as 1
for x in range (1,number+1):
    factorial *= x
    
print(f"{number}! = {factorial}")

