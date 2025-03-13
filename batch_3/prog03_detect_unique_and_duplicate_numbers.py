print("Program 3: Detect Unique and Duplicate Numbers")
numbers = []
# continuously ask the user for input until an invalid input is entered
while True:
    try:
        num = float(input("Enter a number: "))

# check if the numbers is a duplicate
# else if it is unique, add it to the list
# if the input is invalid, break the loop