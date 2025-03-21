print("Program 5: Calculate the Average")
print("Enter a non-numeric value to exit the program.")

numbers = []

while True:
    try:
        num = float(input("Enter a number: "))

        numbers.append(num)
    except ValueError:
        break

if numbers:
    total = sum(numbers)
    average = total / len(numbers)
    print(f"\nAverage: {average:.2f}")
else:
    print("\nNo valid number entered.")