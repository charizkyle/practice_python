# display the program's title
print("Program 4: String Lowercase Checker without using islower()")

# ask the user for a string
string = input("Enter a string: ")

# convert the string to lowercase and compare it with the original
lowercase_string = string.lower()
if string == lowercase_string:
    result = "The string is lowercase."
else:
    result = "The string is not lowercase."
    
# print the result
print()
print(result)