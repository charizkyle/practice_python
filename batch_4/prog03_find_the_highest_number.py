print("Program 3: Find the Highest Number")
print("Enter a non-numeric value to exit the program.")

highest = None

while True:
    try:
        num = float(input("Enter a number: "))
        if highest is None or num > highest:
            highest = num
    except ValueError:
        break

if highest is not None:
    print("\nHighest number:", highest)
else:
    print("\nNo valid number entered.")