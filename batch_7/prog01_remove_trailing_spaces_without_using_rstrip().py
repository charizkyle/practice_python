# display the program title
print("Program 1: Remove Trailing Spaces from String without using rstrip()")

# ask for usere input
string = input("Enter a string with trailing spaces: ")

# remove trailing spaces
i = len(string) - 1
while i >= 0 and string[i] == " ":
    i -= 1

# print result
print()
print(f"'{string[:i + 1]}'")