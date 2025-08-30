# Program 2: Arithmetic Operations using Functions

# Individual function definitions
def add_value(num1, num2):
    return num1 + num2

def sub_value(num1, num2):
    return num1 - num2

def multiply_value(num1, num2):
    return num1 * num2

def divide_value(num1, num2):
    return num1 / num2

# Example usage
num1, num2 = 9, 8
print("Addition:", add_value(num1, num2))
print("Subtraction:", sub_value(num1, num2))
print("Multiplication:", multiply_value(num1, num2))
print("Division:", divide_value(num1, num2))

# Compact version: All operations in one function
def calculate(num1, num2):
    return num1+num2, num1-num2, num1*num2, num1/num2

add, sub, mul, div = calculate(9, 8)
print("Addition:", add)
print("Subtraction:", sub)
print("Multiplication:", mul)
print("Division:", div)
