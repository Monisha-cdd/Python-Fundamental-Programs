# Program: Count total number of digits in a number
num = 123456789
count = 0
while num != 0:
    num = num // 10
    count += 1

print("The total digits are:", count)
