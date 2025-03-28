# display the program's title
print("Program 8: Reverse Casing of String without using swapcase()")

# ask the user for a string
string = input("Enter a string: ")

# reverse the casing of each character in the string
reversed = "".join(char.upper() if char.islower() else char.lower() for char in string)

# print the result
print()
print(reversed)