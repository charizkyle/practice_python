print("Program 9: 0-100 without Multiples of 10 and 5")
num = 0
while num <= 100:
    if num % 10 != 0 and num % 10 != 5:
        print(num)
    num += 1