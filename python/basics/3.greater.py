# Compare 2 numbers and find greater number

num1 = int(input("Enter your first number:"))
num2 = int(input("Enter your second number:"))

if num1 > num2:
    print("The greater number is:", num1)
elif num2 > num1:
    print("The greater number is:", num2)
else:
    print("both numbers are equal")