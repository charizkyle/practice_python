print("Program 4: Find the Lowest Number")
lowest = None

while True:
    try:
        num = float(input("Enter a number: "))

# update the lowest number if the entered number is less than the current lowest number
# stop the loop if an invalid input or non-numeric value is entered