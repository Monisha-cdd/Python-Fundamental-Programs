# Program: Calculate sum of numbers from 1 to 100
num = 100
for i in range(1, num):
    print(i, "+", end=" ")

print(num, "=", sum(range(1, num+1)))
