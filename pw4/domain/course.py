
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

