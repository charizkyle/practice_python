print("Program 4: Sort Numbers in Descending Order")
numbers = []

while True:
    try:
        num = float(input("Enter a number or press Enter to stop: "))

        numbers.append(num)
    except ValueError:
        break
# if the list is not empty, sort the numbers in descending order
# display the numbers from highest to lowest