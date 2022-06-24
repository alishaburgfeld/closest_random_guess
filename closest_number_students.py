import csv
import os
import random
from re import I

def closest_number_students(num):

    random_number=random.randint(1,num)
    print(random_number)

    students = []
    my_path = os.path.abspath(os.path.dirname(__file__))
    path = os.path.join(my_path, "students.csv")

    with open(path, newline="") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            students.append(row)
    
    rolls=[]
    for student in students:
        roll=random.randint(1,num)
        if roll not in rolls:
            rolls.append(roll)
            student["Number"]= roll

    # print(students)
    # print(rolls)
    
    closest=num
    closest_student={}
    for student in students:
        if abs(random_number-int(student["Number"])) < closest:
            closest= abs(random_number-int(student["Number"]))
            # print(f"closest: {closest}")
            closest_student=student
    
    return (closest_student)

print(closest_number_students(100))