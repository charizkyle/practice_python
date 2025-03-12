print("Program 10: 0-100 without ending in zero")

for num in range(101): 
    if num % 10 != 0:
        print(num)