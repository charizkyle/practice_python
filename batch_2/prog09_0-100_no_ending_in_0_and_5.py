print("Program 9: 0-100 without ending in zero/five")
num = 0
while num <= 100:
    if num % 10 != 0 and num % 10 != 5:
        print(num)
    num += 1