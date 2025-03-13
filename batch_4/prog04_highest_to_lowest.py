print("Program 4: Sort Numbers in Descending Order")
numbers = []

while True:
    try:
        num = float(input("Enter a number or press Enter to stop: "))

        numbers.append(num)
    except ValueError:
        break

if numbers:
    numbers.sort()
    print("\nNumbers from highest to lowest:", numbers)
else:
    print("\nNo valid number entered.")