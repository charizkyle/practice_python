# display the program title
print("Program 2: Remove Suffix from String without using removesuffix()")

# input string and suffix to remove
string = input("Enter a string: ")
suffix = input("Enter the suffix to remove: ")

# remove the suffix from the string without using removesuffix()
if string.endswith(suffix):
    string = string.replace(suffix, "", 1)
else:
    string = string # if no suffix is found, print the original string

# print the string without the suffix
print()
print(string)