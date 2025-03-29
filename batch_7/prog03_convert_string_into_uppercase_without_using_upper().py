# display the program's title
print("Program 3: Convert String into Uppercase without using upper()")

# ask the user for a string
string = input("Enter a string: ")

result = ""
for char in string:
    if 'a' <= char <= 'z':
        result += chr(ord(char) - 32)  # convert to uppercase
    else:
        result += char  # keep the character as is

# print the result
print()
print(result)