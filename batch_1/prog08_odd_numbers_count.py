print("Program 8: Odd Numbers Count")
odd_count = 0
odd_numbers = []

for i in range(10):
    num = float(input(f"Enter number {i+1}: "))
    
    if num % 2 != 0:
        odd_count += 1
        odd_numbers.append(num)
        
print()
print(odd_count, "odd numbers")
print(odd_numbers)