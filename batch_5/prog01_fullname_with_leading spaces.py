# display the program's title
print("Program 1: Remove Leading Spaces from Full Name")

# ask the user to input their full name with leading spaces
name = input("Enter your full name with leading spaces: ")

# remove leading spaces
name = name.lstrip()

# print the name without leading spaces
print(f"\nName without leading spaces: {name}")