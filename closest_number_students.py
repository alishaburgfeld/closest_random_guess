import csv
import os
import random

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

    closest= num
    closest_student={}
    rolls=[]
    for student in students:
        roll=random.randint(1,num)
        if roll not in rolls:
            rolls.append(roll)
            student["Number"]= roll
            if abs(random_number-roll) < closest:
                closest= abs(random_number-roll)
                closest_student=student

    print(students)
    # print(rolls)
    
    return (closest_student)

print(closest_number_students(100))