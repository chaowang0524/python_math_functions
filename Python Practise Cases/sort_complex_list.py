students = [
    {"sno": 101, "sname": "Jake", "sgrade": 88},
    {"sno": 103, "sname": "Dan", "sgrade": 92},
    {"sno": 102, "sname": "Bill", "sgrade": 67},
    {"sno": 104, "sname": "Pete", "sgrade": 95},
    {"sno": 105, "sname": "Ashley", "sgrade": 87},

]

students_sorted = sorted(students, key=lambda x: x["sgrade"])

print(students_sorted)
