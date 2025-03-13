print("Calculate the Average")
numbers = []

while True:
    try:
        num = float(input("Enter a number or press Enter to stop: "))

        numbers.append(num)
    except ValueError:
        break
# calculate the average of the numbers in the list
# display the average