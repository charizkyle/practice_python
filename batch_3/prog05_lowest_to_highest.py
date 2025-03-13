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
# display the sorted list