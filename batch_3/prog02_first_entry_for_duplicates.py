print("Program 2: First Entry for Duplicates")
numbers = []

# use a for loop to get 10 numbers from the user
for i in range(10):
    num = float(input(f"Enter number {i+1}: "))
# append the number only if it is not already in the list
# display the first entry for each duplicate number