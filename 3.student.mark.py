import math
import numpy as np

class Student:

    def __init__(self, name, student_id, dob):
        self.__name = name
        self.__id = student_id
        self.__dob = dob
        self.__lib_course_mark = {}
        self.__credits = {}

    def get_name(self):
        return self.__name

    def get_id(self):
        return self.__id

    def get_dob(self):
        return self.__dob

    def input_mark(self, course, mark, credits):
        self.__lib_course_mark[course] = mark  # linking course and mark together
        self.__credits[course] = credits #linking course and credits together

    def get_marks(self):
        return self.__lib_course_mark


    def calculate_gpa(self):
        total_marks = sum(self.__lib_course_mark.values())
        num_of_courses = len(self.__lib_course_mark)
        average_gpa = total_marks / num_of_courses
        return average_gpa

class Course:

    def __init__(self, course_name, course_ID, credit):
        self.__course_name = course_name
        self.__course_ID = course_ID
        self.__credit = credit

    def get_name(self):
        return self.__course_name

    def get_ID(self):
        return self.__course_ID

    def get_credits(self):
        return self.__credit


# Main

#input student informations
num_of_students = int(input("Enter number of students: "))
student_list = []
for i in range(num_of_students):
    name = input(f"Enter student {i + 1}'s name: ")
    student_id = int(input(f"Enter student {i + 1}'s id: "))
    dob = input(f"Enter student {i + 1}'s dob (DD/MM/YYYY): ")
    student_list.append(Student(name, student_id, dob))

#input courses + credits information
num_of_courses = int(input("Enter number of courses: "))
course_list = []
for i in range(num_of_courses):
    course_id = i + 1
    print(f"Course ID {course_id}:")
    course_name = input(f"Enter course {i + 1}'s name: ")
    credit = float(input(f"Enter credits for {course_name}: "))
    course_list.append(Course(course_name, course_id, credit))

#input marks
for student in student_list:
    for course in course_list:
        mark = float(input(f"Enter marks for {student.get_name()} in {course.get_name()}: "))
        student.input_mark(course.get_name(), math.floor(mark), course.get_credits())


#display
for student in student_list:
    print("Student: ", student.get_name(), "\nID: ", student.get_id(), "\nDOB: ", student.get_dob())
    for course in course_list:
        print(f"Mark for {student.get_name()} in {course.get_name()}: {student.get_marks()[course.get_name()]}")

for course in course_list:
    print(f"Credits for the {course.get_name()} course: {course.get_credits()}")

#calculate gpa
for student in student_list:
    print(f"GPA for {student.get_name()}: {student.calculate_gpa()}")

# Sort by GPA in descending order
sorted_list = sorted(student_list, key=lambda student: student.calculate_gpa(), reverse=True)

# Display sorted student list
print("\nSorted Student List by GPA (Descending):")
for student in sorted_list:
    print(f"{student.get_name()}'s GPA: {student.calculate_gpa()}")
