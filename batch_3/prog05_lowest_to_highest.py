# display the program title
print("Program 5: Sort Numbers in Ascending Order")
numbers = []

while True:
    try:
        num = float(input("Enter a number: "))

        numbers.append(num)
    except ValueError:
        break
# sort the list in ascending order
if numbers:
    numbers.sort()
    print("\nNumbers from lowest to highest:", numbers)
else:
    print("\nNo valid number entered.")