# Program: Find students with second lowest score

n = int(input("Enter number of students: "))
records = []
for _ in range(n):
    name = input("Enter name: ")
    mark = float(input("Enter mark: "))
    records.append([name, mark])

scores = [mark for name, mark in records]
lowest = min(scores)

# Remove all lowest scores
while lowest in scores:
    scores.remove(lowest)

second_lowest = min(scores)

# Collect names with second lowest score
names = [name for name, marks in records if marks == second_lowest]

# Print in sorted order
for name in sorted(names):
    print(name)
