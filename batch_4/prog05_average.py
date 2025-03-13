print("Calculate the Average")
numbers = []

while True:
    try:
        num = float(input("Enter a number or press Enter to stop: "))

        numbers.append(num)
    except ValueError:
        break

if numbers:
    total = sum(numbers)
    average = total / len(numbers)
    print(f"\nAverage:", {average:.2f})
else:
    print("\nNo valid number entered.")