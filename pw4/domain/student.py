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

    def input_mark_credits(self, course, mark, credits):
        self.__lib_course_mark[course] = mark  # linking course and mark lib
        self.__credits[course] = credits  # linking course and credits lib

    def get_marks(self):
        return self.__lib_course_mark

    def calculate_gpa(self):
        total_marks = sum(self.__lib_course_mark.values())
        num_of_courses = len(self.__lib_course_mark)
        average_gpa = total_marks / num_of_courses
        return average_gpa


