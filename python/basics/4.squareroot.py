# find the square root of a number
import math

num = int(input("Enter a number:"))

square = int(math.pow(num, 2))
cube = int(math.pow(num, 3))

print("Square of a number", num, "is:", square)
print("Cube of a number", num, "is:", cube)
