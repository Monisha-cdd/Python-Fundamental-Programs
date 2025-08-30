# Program 1: Find Average and Grade using Functions

# Function to calculate average of marks
def average(marks):
    sum_marks = sum(marks)
    total_subjects = len(marks)
    return sum_marks / total_subjects

# Function to check grade from average
def check_grade(avg):
    if avg >= 80:
        grade = "A"
    elif avg >= 70:
        grade = "B"
    elif avg >= 60:
        grade = "C"
    else:
        grade = "FAIL"
    return grade

# Example usage
marks = [90, 78, 68, 98, 87]
avg = average(marks)
print("The average of the given marks:", avg)
print("The grade of given average:", check_grade(avg))
