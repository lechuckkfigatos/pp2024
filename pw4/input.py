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
    return student_list

def course_input(num_of_courses):
    course_list = []
    for course in range(num_of_courses):
        course_id = input(f"Enter course ID: ")
        course_name = input(f"Enter course {course_id}'s name: ")
        credit = float(input(f"Enter credits for {course_name}: "))
        course_list.append(Course(course_name, course_id, credit))
    return course_list

def input_mark(student_list, course_list):
    for student in student_list:
        for course in course_list:
            mark = float(input(f"Enter marks for {student.get_name()} in {course.get_name()}: "))
            student.input_mark_credits(course.get_name(), math.floor(mark), course.get_credits())

