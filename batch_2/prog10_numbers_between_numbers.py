print("Program 10: Numbers between numbers")
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

print("Numbers between", num1, "and", num2, "are:")
for num in range(num1 + 1, num2):
    print(num)