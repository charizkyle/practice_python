# display the program's title
print("Program 7: Adding Zeros at the Beginning without using zfill()")

# input from user
string = input("Enter a string: ")
target_length = int(input("Enter the target length: "))

# add leading zeros using string formatting
result = f"{string:0>{target_length}}"

# display the result
print()
print(result)