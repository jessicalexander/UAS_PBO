from base.User import User
from student import Student
from professor import Professor
from courses import Course
from krs import KRS
import os
from librarian import Librarian
from logger import log_activity

class Admin(User):
    def __init__(self, user_id, name, email, password):
        super().__init__(user_id, name, email, password)

    @log_activity
    def create_user_account(self, user_type, *args):
        if self._logged_in:
            if user_type == "student":
                return Student(*args)
            elif user_type == "professor":
                return Professor(*args)
            elif user_type == "librarian":
                return Librarian(*args)
            else:
                return None
        else:
            print("Admin has to be logged in to do this action")

    @log_activity
    def create_course(self, course_id, course_name, instructor, description="", schedule=""):
        if self._logged_in:
            course = Course(course_id, course_name, instructor, description, schedule)
            return course
        else:
            print("Admin has to be logged in to do this action")
    
    @log_activity
    def assign_professor(self, courses, professor):
        if self._logged_in:
            professor_assigned = False  
            for course in courses:
                if professor._name == course.instructor:
                    professor.teach_course(course)
                    print(f"{professor._name} is assigned to {course.course_name}")
                    professor_assigned = True  
            if not professor_assigned:
                print(f"{professor._name} isn't teaching any of the specified courses.")
        else:
            print("Admin has to be logged in to do this action")

    @log_activity
    def input_billing(self, student, amount):
        if self._logged_in:
            student.billing_amount = (float(amount))
        else:
            print("Admin has to be logged in to do this action")
    
    @log_activity
    def update_semester(self, student, semester):
        if self._logged_in:
            student.semester = semester
        else:
            print("Admin has to be logged in to do this action")
    
    @log_activity
    def add_course_krs(self, courses):
        if self._logged_in:
            for course in courses:
                course_id_prefix = course.course_id[0]
                if course_id_prefix == "1":
                    KRS.krs1.append(course)
                    print(f'Course {course.course_name} is added to KRS 1')
                elif course_id_prefix == "2":
                    KRS.krs2.append(course)
                    print(f'Course {course.course_name} is added to KRS 2')
                elif course_id_prefix == "3":
                    KRS.krs3.append(course)
                    print(f'Course {course.course_name} is added to KRS 3')
                elif course_id_prefix == "4":
                    KRS.krs4.append(course)
                    print(f'Course {course.course_name} is added to KRS 4')
                elif course_id_prefix == "5":
                    KRS.krs5.append(course)
                    print(f'Course {course.course_name} is added to KRS 5')
                else:
                    print('Invalid course ID prefix. Cannot assign to any KRS pack.')
        else:
            print("Admin has to be logged in to do this action")

    @log_activity
    def post_announcement(self, announcement_msg, announcement_system):
        if self._logged_in:
            announcement_system.create_announcement(announcement_msg)
        else:
            print("Admin has to be logged in to do this action")

    @log_activity
    def view_tickets(self, et_system):
        if self._logged_in:
            et_system.view_tickets()
        else:
            print("Admin has to be logged in to do this action")

    @log_activity
    def clear_backlog(self):
        if self._logged_in:
            """Clears the entire backlog."""
            current_dir = os.path.dirname(os.path.abspath(__file__))
            logfile_path = os.path.join(current_dir, 'db', 'backlog.txt')

            with open(logfile_path, 'w') as file:
                file.truncate(0)
            print("Backlog cleared successfully.")
        else:
            print("Admin has to be logged in to do this action")

# admin = Admin(user_id="a1", name="Admin", email="admin@example.com", password="admin123")
# course1 = admin.create_course(course_id="SIWP2005", course_name="Pembelajaraan OOP", instructor="Pak Hendrik", description="Menjadi master dalam OOP", schedule={"Senin": "10.00-12.00", "Selasa": "08.00-10.00"})
# course2 = admin.create_course(course_id="SIWP1001", course_name="Algoritma", instructor="Pak Dave", description="Introduction to programing and algorithms fundamental", schedule={"Senin": "14.00-16.00"})
# print(course1)
# print(course2)

