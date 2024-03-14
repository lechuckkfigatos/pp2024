from domain import student
from domain import course

def student_info_display(student_list, course_list):
    for student in student_list:
        print("Student: ", student.get_name(), "\nID: ", student.get_id(), "\nDOB: ", student.get_dob())
        for course in course_list:
            print(f"Mark for {student.get_name()} in {course.get_name()}: {student.get_marks()[course.get_name()]}")
        print(f"GPA for {student.get_name()}: {student.calculate_gpa()}\n")

def credits_display(course_list):
    for course in course_list:
        print(f"Credits for the {course.get_name()} course: {course.get_credits()}")

def sorted_display(sorted_list):
    print("\nSorted Student List by GPA (Descending):")
    for student in sorted_list:
        print(f"{student.get_name()}'s GPA: {student.calculate_gpa()}")


