# display the program's title
print("Program 6: String Right Spacer without using ljust()")

# ask the user for a string and a target length
string = input("Enter a string: ")
target_length = int(input("Enter the target length: "))

# add spaces to the right of the string until it reaches the target length
if len(string) < target_length:
    string += " " * (target_length - len(string))
else:
    string = string[:target_length] # truncate the string if it is longer than the target length

# print the result
print()
print(f"""'{string}'""")