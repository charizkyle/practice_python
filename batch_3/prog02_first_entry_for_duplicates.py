print("Program 2: First Entry for Duplicates")
numbers = []

for i in range(10):
    num = float(input(f"Enter number {i+1}: "))
    if num not in numbers:
        numbers.append(num)

print(numbers)