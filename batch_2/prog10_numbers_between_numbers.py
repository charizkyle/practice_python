print("Program 10: Numbers between numbers")
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# ensure num1 is the smaller number by swapping values if num1 is greater than num2
if num1 > num2:
    num1, num2 = num2, num1

print("Numbers between", num1, "and", num2, "are:")
for num in range(num1 + 1, num2):
    print(num)