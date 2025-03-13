print("Program 2: Most Frequent Number")
numbers = []

while True:
    try:
        num = float(input("Enter a number or press Enter to stop: "))
        numbers.append(num)
    except ValueError:
        break
# find the most frequent number in the list or a number with most duplicates
if numbers:
    most_frequent = None
    most_frequent_count = 0
    for num in numbers:
        count = numbers.count(num)
        if count > most_frequent_count:
            most_frequent = num
            most_frequent_count = count
# display the most frequent number