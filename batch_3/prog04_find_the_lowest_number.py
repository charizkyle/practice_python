print("Program 4: Find the Lowest Number")
lowest = None

while True:
    try:
        num = float(input("Enter a number: "))
        if lowest is None or num < lowest:
            lowest = num
    except ValueError:
        break