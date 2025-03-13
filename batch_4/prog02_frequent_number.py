print("Program 2: Most Frequent Number")
numbers = []

while True:
    try:
        num = float(input("Enter a number or press Enter to stop: "))
        numbers.append(num)
    except ValueError:
        break

if numbers:
    most_frequent = None
    most_frequent_count = 0
    for num in numbers:
        count = numbers.count(num)
        if count > most_frequent_count:
            most_frequent = num
            most_frequent_count = count

    print("\nMost frequent number:", most_frequent)
    print("Number of duplicates:", most_frequent_count)
else:
    print("\nNo valid number entered.")