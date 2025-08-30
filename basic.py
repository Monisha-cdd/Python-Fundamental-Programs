# Basic Python Programs (No loops, functions, OOPs)

# 1. Add two numbers
a = 5
b = 3
print("Sum:", a + b)   # 8

# 2. Swap two variables
x, y = 10, 20
x, y = y, x
print("After swapping: x =", x, ", y =", y)   # x=20, y=10

# 3. Check even or odd
num = 7
if num % 2 == 0:
    print(num, "is Even")
else:
    print(num, "is Odd")

# 4. Find maximum of three numbers
a, b, c = 12, 8, 15
print("Maximum number is:", max(a, b, c))   # 15

# 5. Convert Celsius to Fahrenheit
celsius = 37
fahrenheit = (celsius * 9/5) + 32
print("Fahrenheit:", fahrenheit)   # 98.6

# 6. Simple interest calculation
p, r, t = 1000, 5, 2   # principal, rate, time
si = (p * r * t) / 100
print("Simple Interest:", si)   # 100.0

# 7. Area of circle
radius = 7
pi = 3.14159
print("Area of circle:", pi * radius * radius)   # 153.93791

# 8. Reverse a string
text = "Monisha"
print("Reversed string:", text[::-1])   # ahsinoM

# 9. ASCII value of a character
ch = 'A'
print("ASCII value of", ch, "is", ord(ch))   # 65

# 10. Check positive, negative or zero
n = -5
if n > 0:
    print("Positive")
elif n < 0:
    print("Negative")
else:
    print("Zero")
