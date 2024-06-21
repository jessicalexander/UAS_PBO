from base.User import User
from courses import Course
from logger import log_activity

class Professor(User):
    def __init__(self, user_id, name, email, password):
        super().__init__(user_id, name, email, password)
        self.courses_taught = []

    @log_activity
    def teach_course(self, course):
        self.courses_taught.append(course)

    @log_activity
    def post_grade(self, input_course_name, student, grade):
        found_course = next((course for course in self.courses_taught if course.course_name.lower() == input_course_name.lower()), None)
        if found_course:
            found_course.set_grade(student, grade)
        else:
            print(f"You are not teaching the course {input_course_name.title()}")

    @log_activity
    def post_attendance(self, input_course_name, student, attendance):
        found_course = next((course for course in self.courses_taught if course.course_name.lower() == input_course_name.lower()), None)
        if found_course:
            found_course.set_attendance(student, attendance)
        else:
            print(f"You are not teaching the course {input_course_name.title()}")

    @log_activity
    def post_exam_schedule(self, input_course_name, date):
        found_course = next((course for course in self.courses_taught if course.course_name.lower() == input_course_name.lower()), None)
        if found_course:
            found_course.set_exam_schedule(date)
        else:
            print(f"You are not teaching the course {input_course_name.title()}")

    @log_activity
    def post_course_material(self, input_course_name, material):
        found_course = next((course for course in self.courses_taught if course.course_name.lower() == input_course_name.lower()), None)
        if found_course:
            found_course.set_course_material(self._name, material)
        else:
            print(f"You are not teaching the course {input_course_name.title()}")


    