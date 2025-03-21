print("Program 5: Remainder")
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

if num2 == 0:
    print("\nDivision by zero is UNDEFINED.")
else:
    rem = num1 % num2
    print()
    print("=", rem)