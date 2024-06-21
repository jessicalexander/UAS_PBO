from base.User import User
from courses import Course
from logger import log_activity

class Student(User):
    def __init__(self, user_id, name, email, password, semester):
        super().__init__(user_id, name, email, password)
        self.course_list = []  # List of Course objects
        self.grade_list = {}   # List of Grade objects
        self.billing_amount = 0
        self.semester = semester
        self.krs = ""
        self.soft_point = 0
        self.certificates = []

    @log_activity
    def join_course(self, input_course_id, courses):
        if not input_course_id:
            print("Please provide a course code.")
            return False
        if self.krs == "paket":
            print("You have picked 'KRS paket', you can't join a class")
            return
        for course in courses:
            if course.course_id == input_course_id:
                self.course_list.append(course)
                Course.add_student(course, self._name)
                print(f'{self._name} has joined {course.course_name}')
                return True
        print("Course not found.")
        return False
    
    @log_activity
    def view_grades(self):
        if not self.course_list:
            print(f"You have yet to join a course")
            return
        print(f"Grades for {self._name}:")
        for course in self.course_list:
            if self._name in course.course_grades:
                print(f"Course: {course.course_name}, Grade: {course.course_grades[self._name]}")
            else:
                print(f"No grade available for course: {course.course_name}")

    @log_activity
    def view_attendance(self):
        if not self.course_list:
            print(f"You have yet to join a course")
            return
        print(f"Attendances for {self._name}:")
        
        for course in self.course_list:
            if self._name in course.course_attendance:
                print(f"Course: {course.course_name}, attendance: {course.course_attendance[self._name]}")
            else:
                print(f"Your professor has not post attendance for course: {course.course_name}")

    @log_activity
    def view_courses(self):
        if not self.course_list:
            print(f"You have yet to join a course")
            return
        print(f"These are your courses:")
        for course_list in self.course_list:
            for course in course_list:
                print(course)

    @log_activity
    def view_exam_schedule(self):
        if not self.course_list:
            print(f"You have yet to join a course")
            return
        for course in self.course_list:
            if not course.exam_schedule:
                print(f"The course {course.course_name} has yet to schedule an exam")
                return
            print(f"Course: {course.course_name}, exam on {course.exam_schedule}")

    @log_activity
    def view_course_materials(self):
        if not self.course_list:
            print(f"You have yet to join a course")
            return
        for course in self.course_list:
            if not course.course_materials:
                print(f"The course {course.course_name} has no course material currently")
            elif len(course.course_materials) == 1:
                print(f"Course: {course.course_name}, material: {course.course_materials}")
            else:
                print(f"Course: {course.course_name}, materials: {course.course_materials}")
    
    @log_activity
    def view_billing(self):
        print(f'Billing amount for {self._name} is Rp.{self.billing_amount}')

    @log_activity
    def submit_certificate(self, certificate, certificate_type):
        if certificate.lower() in [certificate.lower() for c in self.certificates]:
            print("You have posted the same certificate")
            return
        self.certificates.append(certificate)
        if certificate_type.lower() == "menang lomba":
            self.soft_point += 50
            print("You got 50 softskill point")
        elif certificate_type.lower() == "psmb":
            self.soft_point += 120
            print("You got 120 softskill point")
        else:
            self.soft_point += 5
            print("You got 5 softskill point")



        



# course1 = Course(course_id="SIWP2005", course_name="Pembelajaraan OOP", instructor="Pak Hendrik", description="Menjadi master dalam OOP", schedule={"Senin": "10.00-12.00", "Selasa": "08.00-10.00"})
# course2 = Course(course_id="SIWP1001", course_name="Algoritma", instructor="Pak Dave", description="Introduction to programing and algorithms fundamental", schedule={"Senin": "14.00-16.00"})

# courses = [course1, course2]

# student = Student("SSI1", "peter", "peter@si.ukrida.ac.id", "studentpass")
# student1 = Student("SSI2", "jesica", "jesica@si.ukrida.ac.id", "studentpass1")

# student.join_course("SIWP1001", courses)
# student1.join_course("SIWP2005", courses)
# student1.join_course("SIWP2015", courses)
# student1.join_course("",courses)
# print(course1.students_joined)