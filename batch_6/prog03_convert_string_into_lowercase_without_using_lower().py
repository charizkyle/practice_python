# display the program's title
print("Program 3: Convert String into Lowercase without using lower()")

# input string
string = input("Enter a string: ")

# use str.casefold() to convert to lowercase (alternative to lower())
result = string.casefold()

# print the string in lowercase
print()
print(result)