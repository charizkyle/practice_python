# display the program's title
print("Program 5: String Prefix Checker without using startswith()")

# ask the user for a string and a prefix to check
string = input("Enter a string: ")
prefix = input("Enter the prefix to check: ")

# check if the string starts with the given prefix
if string [:len(prefix)] == prefix:
    result = "The string starts with the given prefix."
else:
    result = "The string does not start with the given prefix."

# print the result
print()
print(result)