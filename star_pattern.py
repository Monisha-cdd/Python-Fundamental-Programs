# Program: Print star pyramid pattern

row = 6
for i in range(1, row+1):
    for space in range(row - i):
        print(" ", end=" ")
    for pattern in range(1, i+1):
        print("* ", end=" ")
    print()
