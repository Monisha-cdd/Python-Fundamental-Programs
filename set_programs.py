# Program: Set Operations Example

set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

print("Set1:", set1)   # {1, 2, 3, 4}
print("Set2:", set2)   # {3, 4, 5, 6}

# 1. Union
print("Union:", set1 | set2)   # {1, 2, 3, 4, 5, 6}

# 2. Intersection
print("Intersection:", set1 & set2)   # {3, 4}

# 3. Difference
print("Difference (set1 - set2):", set1 - set2)   # {1, 2}
print("Difference (set2 - set1):", set2 - set1)   # {5, 6}
