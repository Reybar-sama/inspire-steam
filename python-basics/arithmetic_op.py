# Name : Rey Bar
# Date : 17/02/2026
# Program to perform arithmetic operations

f_number = 12
s_number = 34
sum_number = f_number + s_number
diff_number = f_number - s_number
prod_number = f_number * s_number
quot_number = f_number / s_number


print("The sum of the numbers is: %d"%sum_number)
print("The quotient of the numbers is: %0.2f "%quot_number)

# modulus - remainder
print(7%5)

# for even and odd numbers
for x in range(0,21):
    if (x%2 == 1):
        print(f"{x} is odd")
    elif (x%2 ==0):
        print(f"{x} is even")
