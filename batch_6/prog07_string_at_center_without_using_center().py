# display the program's title
print("Program 7: String at Center without using center()")

# ask the user for a string and a target length
string = input("Enter a string: ")
target_length = int(input("Enter the target length: "))

# center the string with spaces on both sides
result = f"{string:^{target_length}}"

# print the result
print()
print(f"""'{result}'""")