# display the program's title
print("Program 10: Full Name in Snake Case")

# ask the user for their full name with incorrect casing
full_name = input("Enter your full name with incorrect casing: ")

# convert to snake case
snake_case = full_name.lower().replace(" ", "_")

# print the full name in snake case
print("\nFull name in snake case:", snake_case)