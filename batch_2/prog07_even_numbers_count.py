print("Program 7: Even Numbers Count")
even_count = 0
even_numbers = []

for i in range(10):
    num = float(input(f"Enter number {i+1}: "))

    if num % 2 == 0:
        even_count += 1
        even_numbers.append(num)

print()
print(even_count, "even numbers")
print(even_numbers)