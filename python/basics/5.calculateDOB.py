from datetime import datetime

# current year
currentYear = datetime.now().year

userdob = int(input("Enter your birth year: "))
username = str(input("Enter your first name: "))

# calculating age
age = currentYear - userdob

print(username, ", your age is: ", age)