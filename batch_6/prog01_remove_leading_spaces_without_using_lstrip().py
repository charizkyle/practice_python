# display the program title
print("Program 1: Remove Leading Spaces from String without using lstrip()")

# input string with leading spaces
string = input("Enter a string with leading spaces: ")

# strip each leading spaces using replace()
while string.startswith(" "):
    string = string.replace(" ", "", 1)

# print the string without leading spaces
print()
print(string)