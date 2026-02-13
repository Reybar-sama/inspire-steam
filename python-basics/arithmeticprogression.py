# Name : Rey Bar
# Date : 13/02/2026
# Program to calculate arithmetic progression in Python.

# Calculating the nth term

a = int(input("Enter the first term:"))
n = int(input("Enter the number of terms:"))
d = int(input("Enter the common difference:"))

nth_term = a+(n-1)*d
print(f"The nth term is : {nth_term}")

sn = (n / 2) *((2*a) +(n-1)*d)

print(f"The arithmetic sum is: ",sn)