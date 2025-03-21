print("Program 4: Sort Numbers in Descending Order")
print("Enter a non-numeric value to exit the program.")

numbers = []

while True:
    try:
        num = float(input("Enter a number: "))
        numbers.append(num)
    except ValueError:
        break

if numbers:
    numbers.sort(reverse=True)
    print("\nNumbers from highest to lowest:", numbers)
else:
    print("\nNo valid number entered.")