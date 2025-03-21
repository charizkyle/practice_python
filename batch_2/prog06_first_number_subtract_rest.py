print("Program 6: 1st Number Subtract Rest")
numbers = []
for i in range(10):
    num = float(input(f"Enter number {i+1}: "))
    numbers.append(num)

result = numbers[0] - sum(numbers[1:])
print()
print("=", result)