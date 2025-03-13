# display the program title
print("Program 1: Duplicate Numbers")
numbers = []
duplicates = []

for i in range(10):
    num = float(input(f"Enter number {i+1}: "))
    numbers.append(num)

for num in numbers:
    if numbers.count(num) > 1 and num not in duplicates:
        duplicates.append(num)

# display the result