from datetime import datetime

class Course:
    def __init__(self, course_id, course_name, instructor, description, schedule):
        self.course_id = course_id
        self.course_name = course_name
        self.description = description
        self.instructor = instructor
        self.schedule = schedule
        self.students_joined = []  
        self.course_materials = []
        self.course_grades ={}
        self.course_attendance ={}
        self.exam_schedule = ""
    def add_student(self, student_name):
        self.students_joined.append(student_name)

    def __str__(self):
        return f"Course ID: {self.course_id}, Name: {self.course_name}, Instructor: {self.instructor}, Description: {self.description}, Schedule: {self.schedule}"

    def set_grade(self, student, grade):
        if student not in self.students_joined:
            print("Student is not in this class")
            return
        self.course_grades[student] = grade
        print(f'{self.course_name} grades: {self.course_grades}')

    def set_attendance(self, student, attendance):
        if student not in self.students_joined:
            print("Student is not in this class")
            return
        timestamp = datetime.now()
        formatted_timestamp = timestamp.strftime("%Y-%m-%d")

        self.course_attendance[student] = {formatted_timestamp : attendance}
        print(f'{self.course_name} attendance : {self.course_attendance}')
    
    def set_exam_schedule(self, date):
        self.exam_schedule = date
        print(f'{self.course_name} scheduled an exam on {date}')

    def set_course_material(self, professor, material):
        self.course_materials.append(material)
        print(f'{professor} posted a material "{material}"')

    def get_student_list(self):
        print(f'Students in the class {self.course_name} : {self.students_joined}')
    

# course1 = Course(course_id="SIWP1001", course_name="Algoritma", instructor="Pak Dave", description="Introduction to programing and algorithms fundamental", schedule={"Senin": "14.00-16.00"})
# course2 = Course(course_id="SIWP2005", course_name="Pembelajaraan OOP", instructor="Pak Hendrik", description="Menjadi master dalam OOP", schedule={"Senin": "10.00-12.00", "Selasa": "08.00-10.00"})

# print(course1)
# print(course2)

