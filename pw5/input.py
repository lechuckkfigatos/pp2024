import math
from domain.student import Student
from domain.course import Course


def student_input(num_of_students):
    student_list = []
    for i in range(num_of_students):
        name = input(f"Enter student {i + 1}'s name: ")
        student_id = int(input(f"Enter student {i + 1}'s id: "))
        dob = input(f"Enter student {i + 1}'s dob (DD/MM/YYYY): ")
        student_list.append(Student(name, student_id, dob))

        student_file = open("student.txt", 'w')
        for student in student_list:
            student_file.write(f"\nStudent name: {student.get_name()}\nStudent ID: {student.get_id()}\nStudent DOB: {student.get_dob()}\n")

    return student_list

def course_input(num_of_courses):
    course_list = []
    for course in range(num_of_courses):
        course_id = input(f"Enter course ID: ")
        course_name = input(f"Enter course {course_id}'s name: ")
        credit = float(input(f"Enter credits for {course_name}: "))
        course_list.append(Course(course_name, course_id, credit))

        course_file = open("courses.txt", 'w')
        course_file.write('\n')
        for course in course_list :
            course_file.write(f"\nCourse name: {course.get_name()}\nCourse ID: {course.get_ID()}\nCourse Credits: {course.get_credits()}\n")

    return course_list

def input_mark(student_list, course_list):
    mark_file = open('mark.txt', 'w')
    for student in student_list:
        for course in course_list:
            mark = float(input(f"Enter marks for {student.get_name()} in {course.get_name()}: "))
            student.input_mark_credits(course.get_name(), math.floor(mark), course.get_credits())


            mark_file.write(f"{student.get_name()}'s mark in {course.get_name()}: {student.get_marks()[course.get_name()]}\n")



