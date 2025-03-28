# display the program's title
print("Program 10: Title Casing for Each Word in the String without using title()")

# ask the user for a string
string = input("Enter a string: ")

# split the string into words and apply title casing to each word
result = " ".join(word.capitalize() for word in string.split())

# print the result
print()
print(result)