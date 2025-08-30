# Program: Return list of squares using functions
def squares(n):
    return [i**2 for i in range(1, n+1)]

print("Squares up to 5:", squares(5))
