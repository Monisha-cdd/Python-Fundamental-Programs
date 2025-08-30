# Program: List Methods Example

numbers = [10, 20, 30, 40]
print("Original List:", numbers)   # [10, 20, 30, 40]

# 1. append()
numbers.append(50)
print("After append(50):", numbers)   # [10, 20, 30, 40, 50]

# 2. insert()
numbers.insert(2, 25)
print("After insert(2, 25):", numbers)   # [10, 20, 25, 30, 40, 50]

# 3. remove()
numbers.remove(30)
print("After remove(30):", numbers)   # [10, 20, 25, 40, 50]

# 4. pop()
popped = numbers.pop()
print("After pop():", numbers, "| Popped element:", popped)  # [10, 20, 25, 40] | 50

# 5. reverse()
numbers.reverse()
print("After reverse():", numbers)   # [40, 25, 20, 10]

# 6. count()
print("Count of 20:", numbers.count(20))   # 1

# 7. slicing
print("Slicing [1:3]:", numbers[1:3])   # [25, 20]

# 8. split() (works with string, not list)
text = "apple,banana,cherry"
fruits = text.split(",")
print("Split string into list:", fruits)   # ['apple', 'banana', 'cherry']
