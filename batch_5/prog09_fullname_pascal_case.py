# display the program's title
print("Program 9: Full Name in Pascal Case")

# ask the user for their full name with incorrect casing
full_name = input("Enter your full name with incorrect casing: ")

# convert to pascal case
pascal_case = full_name.title().replace(" ", "")

# print the full name in pascal case
print("\nFull name in pascal case:", pascal_case)