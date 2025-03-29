# display the program's title
print("Program 8: Substring Counter without using count()")

# ask the user for a main string and a substring
main_string = input("Enter the main string: ")
substring = input("Enter the substring to count: ")

# count the occurrences of the substring in the main string
count = 0
index = main_string.find(substring)
while index != -1:
    count += 1
    index = main_string.find(substring, index + 1)

# display the result
print()
print(f"The substring '{substring}' occurs {count} times in the main string.")