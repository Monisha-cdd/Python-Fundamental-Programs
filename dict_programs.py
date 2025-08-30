# 1. Basic dictionary creation
student = {"name": "Monisha", "age": 19, "dept": "IT"}
print("Student Dictionary:", student)   
# {'name': 'Monisha', 'age': 19, 'dept': 'IT'}

# 2. Access values using keys
print("Name:", student["name"])   # Monisha
print("Department:", student["dept"])   # IT

# 3. Add new key:value
student["grade"] = "A"
print("After adding grade:", student)   
# {'name': 'Monisha', 'age': 19, 'dept': 'IT', 'grade': 'A'}

# 4. Update value
student["age"] = 20
print("After updating age:", student)   
# {'name': 'Monisha', 'age': 20, 'dept': 'IT', 'grade': 'A'}

# 5. Delete key:value
del student["dept"]
print("After deleting dept:", student)   
# {'name': 'Monisha', 'age': 20, 'grade': 'A'}

# 6. Loop through dictionary
print("\nIterating through dictionary:")
for key, value in student.items():
    print(key, ":", value)

# 7. Dictionary comprehension
squares = {x: x**2 for x in range(1, 6)}
print("Squares dictionary:", squares)   
# {1:1, 2:4, 3:9, 4:16, 5:25}

# 8. Nested dictionary (like your trip example)
trip_details = {
   "A": {"trip_id": "UB12345", "pickup": "Chennai", "drop": "Airport", "fare": 350.09},
   "B": {"trip_id": "UB678", "pickup": "Mysore", "drop": "Tambaram", "fare": 600.09},
   "C": {"trip_id": "UB910", "pickup": "Delhi", "drop": "Maharashtra", "fare": 2500}
}

print("\nPickup point of trip A:", trip_details["A"]["pickup"])   # Chennai

for trip_id, details in trip_details.items():
    print(details["trip_id"], ":", details["pickup"], "--->", details["drop"])
