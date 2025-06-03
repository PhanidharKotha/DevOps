# find the greater number between 2 numbers using "max" function

import math

# Input two numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Find the greater number using the built-in max() function
greater = int(max(num1,num2))

print(f"The greater number is: {greater}")