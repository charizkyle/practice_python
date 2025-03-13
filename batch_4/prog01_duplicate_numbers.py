print("Program 1: Duplicate Numbers in 10 Numbers")
print("Enter a non-numeric value to exit the program.")
numbers = []
duplicates = []

for i in range(10):
    num = float(input(f"Enter number {i+1}: "))
    numbers.append(num)

for num in numbers:
    if numbers.count(num) > 1 and num not in duplicates:
        duplicates.append(num)

if duplicates:
    print("\nDuplicate numbers:", duplicates)
else:
    print("\nNo duplicate numbers found")