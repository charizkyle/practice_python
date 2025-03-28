# display the program's title
print("Program 4: String Uppercase Checker without using isupper()")

# ask the user for a string
string = input("Enter a string: ")

# convert the string to uppercase and compare it with the original
uppercase_string = string.upper()
if string == uppercase_string:
    result = "The string is uppercase."
else:
    result = "The string is not uppercase."
    
# print the result
print()
print(result)