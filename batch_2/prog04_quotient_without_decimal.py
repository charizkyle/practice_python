print("Program 4: Quotient of 2 Numbers without Decimal")
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

if num2 == 0:
    print("\nDivision by zero is UNDEFINED.")
else:
    quotient = int(num1 / num2)
    print()
    print(quotient)