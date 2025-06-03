# Import just the function from def_greater.py (used when you only need one function from the module)
from def_greater import greater_num

# Define two numbers
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Call the function and print the result
greater = greater_num(num1, num2)

print("The greater number is:", greater)