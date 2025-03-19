# display the program's title
print("Program 2: Format Numbers in 6 Digits")

# ask the user for a number between 0 and 1000
number = int(input("Enter a number between 0 and 1000: "))

# format the number to have 6 digits
formatted_number = f"{number:06d}"

# print the formatted number
print(f"\nFormatted number: {formatted_number}")