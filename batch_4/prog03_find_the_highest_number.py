# display program title
print("Program 3: Find the Highest Number")
highest = None

while True:
    try:
        num = float(input("Enter a number or press Enter to stop: "))
        if highest is None or num > highest:
            highest = num
    except ValueError:
        break
    
# display the highest number if any number was entered