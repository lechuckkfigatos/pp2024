class Student:

    def __init__(self, name, student_id, dob):
        self.__name = name
        self.__id = student_id
        self.__dob = dob
        self.__lib_course_mark = {}

    def get_name(self):
        return self.__name

    def get_id(self):
        return self.__id

    def get_dob(self):
        return self.__dob

    def input_mark(self, course, mark):
        self.__lib_course_mark[course] = mark  #linking course and mark together

    def get_marks(self):
        return self.__lib_course_mark

class Course:

    def __init__(self, course_name, course_ID):
        self.__course_name = course_name
        self.__course_ID = course_ID

    def get_name(self):
        return self.__course_name

    def get_ID(self):
        return self.__course_ID


def display(student, course):
    print("Student: ", student.get_name(), "\nID: ", student.get_id(), "\nDOB: ", student.get_dob())
    print(f"Mark for {student.get_name()} in : ")
    course_mark = student.get_marks()
    for course_name, mark in course_mark.items():
        print(f"{course_name}: {mark}")


# Main

num_of_students = int(input("Enter number of students: "))
student_list = []
for i in range(num_of_students):
    name = input(f"Enter student {i + 1}'s name: ")
    student_id = int(input(f"Enter student {i + 1}'s id: "))
    dob = input(f"Enter student {i + 1}'s dob (DD/MM/YYYY): ")
    student_list.append(Student(name, student_id, dob))

num_of_courses = int(input("Enter number of courses: "))
course_list = []
for i in range(num_of_courses):
    course_id = i + 1
    print(f"Course ID {course_id}:")
    course_name = input(f"Enter course {i + 1}'s name: ")
    course_list.append(Course(course_name, course_id))

for student in student_list:
    for course in course_list:
        mark = input(f"Enter marks for {student.get_name()} in {course.get_name()}: ")
        student.input_mark(course.get_name(), mark)

for student in student_list:
    print("Student: ", student.get_name(), "\nID: ", student.get_id(), "\nDOB: ", student.get_dob())
    for course in course_list:
        print(f"Mark for {student.get_name()} in {course.get_name()}: {student.get_marks()[course.get_name()]}")
    
