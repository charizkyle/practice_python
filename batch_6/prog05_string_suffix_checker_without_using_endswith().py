# display the program's title
print("Program 5: String Suffix Checker without using endswith()")

# ask the user for a string and a suffix to check
string = input("Enter a string: ")
suffix = input("Enter the suffix to check: ")

# check if the string ends with the given suffix
if string[-len(suffix):] == suffix:
    result = "The string ends with the given suffix."
else:
    result = "The string does not end with the given suffix."

# print the result
print()
print(result)