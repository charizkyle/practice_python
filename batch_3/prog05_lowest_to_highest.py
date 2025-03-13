print("Program 5: Sort Numbers in Ascending Order")
print("Enter a non-numeric value to exit the program.")

numbers = []

while True:
    try:
        num = float(input("Enter a number: "))

        numbers.append(num)
    except ValueError:
        break

if numbers:
    numbers.sort()
    print("\nNumbers from lowest to highest:", numbers)
else:
    print("\nNo valid number entered.")