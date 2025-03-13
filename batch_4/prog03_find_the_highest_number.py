print("Program 3: Find the Highest Number")
highest = None

while True:
    try:
        num = float(input("Enter a number or press Enter to stop: "))
        if highest is None or num > highest:
            highest = num
    except ValueError:
        break

if highest is not None:
    print("\nHighest number:", highest)
else:
    print("\nNo valid number entered.")