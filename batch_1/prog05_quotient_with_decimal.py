print("Program 5: Quotient of 2 Numbers with Decimal")
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

if num2 == 0:
    print("\nDivision by zero is UNDEFINED.")
else:
    quotient = num1 / num2
    print()
    print(f"= {quotient:.2f}")