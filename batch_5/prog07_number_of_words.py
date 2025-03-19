# display the program's title
print("Program 7: Number of Words in a Statement")

# ask the user to input a complete statement
statement = input("Enter a complete statement: ")

# split the statement into words and count the number of words
word_count = len(statement.split())

# print the number of words in the statement
print("\nNumber of words in the statement:", word_count)