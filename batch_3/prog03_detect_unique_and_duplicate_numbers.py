print("Program 3: Detect Unique and Duplicate Numbers")
print("Enter a non-numeric value to exit the program.")
numbers = []

while True:
    try:
        num = float(input("Enter a number: "))

        if num in numbers:
            print("Duplicate")
        else:
            print("Unique")
            numbers.append(num)
    except ValueError:
        print("Invalid input. Exiting the program.")
        break