print("Program 1: Numbers without duplicates")
numbers = []
for i in range(10):
    num = float(input(f"Enter number {i+1}: "))
    numbers.append(num)

unique_numbers = [num for num in numbers if numbers.count(num) == 1]
print("\nNumbers without duplicates:", unique_numbers)