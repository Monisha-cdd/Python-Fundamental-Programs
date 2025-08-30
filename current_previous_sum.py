# Program: Print current and previous number sum
print("Printing current and previous number sum in range(10)")
previous = 0
for i in range(10):
    print("Current number:", i, "Previous number:", previous, "Sum:", i+previous)
    previous = i
