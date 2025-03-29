# display the program's title
print("Program 9: Finding the First Location of Substring without using index()")

# ask the user for a string and a substring
string = input("Enter a string: ")
substring = input("Enter the substring to find: ")

# find the first occurrence of the substring using find()
index = string.find(substring)

# if the substring is found, print its index; otherwise, print a message
if index != -1:
    print()
    print(f"The first location of '{substring}' is at index {index}.")
else:
    print()
    print(f"'{substring}' was not found in the string.")