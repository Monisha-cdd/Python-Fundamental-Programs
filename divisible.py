# Program: Display numbers from list based on conditions
# - Divisible by 5
# - Skip if > 150
# - Stop if > 500

numbers = [12, 75, 150, 180, 145, 525, 50]
for i in numbers:
    if i > 500:
        break
    elif i > 150:
        continue
    elif i % 5 == 0:
        print(i)
