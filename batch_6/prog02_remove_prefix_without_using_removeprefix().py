# display the program title
print("Program 2: Remove Prefix from String without using removeprefix()")

# input string and prefix to remove
string = input("Enter a string: ")
prefix = input("Enter the prefix to remove: ")

# remove the prefix from the string without using removeprefix()
if string.startswith(prefix):
    string = string.replace(prefix, "", 1)
else:
    string = string # if no prefix is found, print the original string

# print the string without the prefix
print()
print(string)