from input import student_input, course_input, input_mark
from output import student_info_display, credits_display, sorted_display


num_of_students = int(input("Enter number of students: "))
student_list = student_input(num_of_students)

num_of_courses = int(input("Enter number of courses: "))
course_list = course_input(num_of_courses)

input_mark(student_list, course_list)

student_info_display(student_list, course_list)

credits_display(course_list)

sorted_list = sorted(student_list, key=lambda student: student.calculate_gpa(), reverse=True)

sorted_display(sorted_list)

