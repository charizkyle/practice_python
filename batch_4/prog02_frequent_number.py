print("Program 2: Most Frequent Number")
numbers = []

while True:
    try:
        num = float(input("Enter a number or press Enter to stop: "))
        numbers.append(num)
    except ValueError:
        break
# find the most frequent number in the list or a number with most duplicates
# display the most frequent number