# display the program's title
print("Program 6: Full Name with Reversed Casing")

# ask the user to input their full name with incorrect casing
full_name = input("Enter your full name with incorrect casing: ")

# reverse the caasing of each character in the full name
reversed = "".join(char.upper()if char.islower() else char.lower() for char in full_name)

# print the full name with reversed casing
print("\nFull name with reversed casing", reversed)