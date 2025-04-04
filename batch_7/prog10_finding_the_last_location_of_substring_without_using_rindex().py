# display the program's title
print("Program 10: Finding the Last Location of Substring without using rindex()")

# ask the user for a string and a substring
string = input("Enter a string: ")
substring = input("Enter the substring to find: ")

# find the last occurrence of the substring using rfind()
index = string.rfind(substring)

# if the substring is found, print its index; otherwise, print a message
if index != -1:
    print()
    print(f"The last location of '{substring}' is at index {index}.")
else:
    print()
    print(f"'{substring}' was not found in the string.")