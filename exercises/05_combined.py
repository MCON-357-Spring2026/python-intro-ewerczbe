"""
TODO:
Dictionary of students -> grades
Print averages
"""
students = {
    "Chaim" : [90, 95, 100], "Moshe": [70, 75, 80], "David": [98, 76, 54]
}
for student, grades in students.items():
    average = sum(grades) / len(grades)
    print(student, "average:", average)