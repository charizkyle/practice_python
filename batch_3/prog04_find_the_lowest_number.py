print("Program 4: Find the Lowest Number")
print("Enter a non-numeric value to exit the program.")
lowest = None

while True:
    try:
        num = float(input("Enter a number: "))
        if lowest is None or num < lowest:
            lowest = num
    except ValueError:
        break

# display the lowest number
if lowest is not None:
    print("\nLowest number:", lowest)
else:
    print("\nNo valid number entered.")