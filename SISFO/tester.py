from admin import Admin
from krs import KRS
from courses import Course
from eticket import ETicketSystem
from announcement import announcementSystem
from book import Book
from library import Library


def main():
    admin = Admin("A1", "Monica", "monica@si.ukrida.ac.id", "adminpass")
    admin.login("monica@si.ukrida.ac.id", "adminpass")


    # instantiate
    """
    args:
        - user type: "student or professor"
        - user_id, name, email, and password for user object
        example: 
        - ("user_type", "user_id", "name", "email", "password")
        - for user_type == student, ("user_type", "user_id", "name", "email", "password", semester)
        - admin.create_user_account("student", "S1", "peter", "peter@si.ukrida.ac.id", "studentpass", 1)
        - professor and librarian ("user_type", "user_id", "name", "email", "password")
    """
    # # admin creates user test
    student = admin.create_user_account("student", "SSI1", "peter", "peter@si.ukrida.ac.id", "studentpass", 1)
    # student1 = admin.create_user_account("student", "SSI2", "jesica", "jesica@si.ukrida.ac.id", "studentpass1", 1)
    # professor = admin.create_user_account("professor", "P1", "Dr. Hendrik", "example@ukrida.ac.id", "profpass")
    # professor1 = admin.create_user_account("professor", "P2", "Dr. Dave", "example1@ukrida.ac.id", "profpass1")
    # librarian = admin.create_user_account("librarian", "L1", "John", "john@example.com", "librarianpass")

    # # login test
    # for user in [student, student1, professor]:
    #     if user:
    #         print(f'{user._name} : {user.login(user._email, user._password)}')

    # # logout test
    # for user in [student, student1, professor]:
    #     if user:
    #         print(f'{user._name} : {user.logout()}')
    
    # # course test
    # c1 = admin.create_course(course_id="1SIWP2005", course_name="Pembelajaraan OOP", instructor="Dr. Hendrik", description="Menjadi master dalam OOP", schedule={"Senin": "10.00-12.00", "Selasa": "08.00-10.00"})
    # c2 = admin.create_course(course_id="1SIWP1001", course_name="Algoritma", instructor="Dr. Dave", description="Introduction to programing and algorithms fundamental", schedule={"Senin": "14.00-16.00"})
    # c3 = admin.create_course(course_id="3SIWP9001", course_name="Software Engineering", instructor="Pak Adi", description="Principles and practices of software development", schedule={"Selasa": "10.00-12.00", "Kamis": "10.00-12.00"})
    # c4 = admin.create_course(course_id="3SIWP0001", course_name="Introduction to Computer Science", instructor="Dr. Maria", description="Foundational concepts of computer science and programming", schedule={"Senin": "08.00-10.00", "Rabu": "08.00-10.00"})
    # c5 = admin.create_course(course_id="5SIWP3003", course_name="Data Science", instructor="Dr. Sarah", description="Exploring data science concepts and techniques", schedule={"Rabu": "13.00-15.00", "Kamis": "10.00-12.00"})
    # c6 = admin.create_course(course_id="2PISA1001", course_name="Web Development", instructor="Pak Budi", description="Building dynamic websites using modern web technologies", schedule={"Jumat": "09.00-11.00", "Sabtu": "13.00-15.00"})
    # c7 = admin.create_course(course_id="2PISA1002", course_name="Mobile App Development", instructor="Dr. Alex", description="Creating mobile applications for iOS and Android platforms", schedule={"Senin": "16.00-18.00", "Rabu": "16.00-18.00"})
    # c8 = admin.create_course(course_id="4PISA1002", course_name="Database Management", instructor="Pak Joko", description="Understanding database concepts and SQL programming", schedule={"Selasa": "13.00-15.00", "Kamis": "13.00-15.00"})    
    # c9 = admin.create_course(course_id="4PISA1002", course_name="Network Security", instructor="Dr. Lisa", description="Securing computer networks from cyber threats", schedule={"Rabu": "09.00-11.00", "Jumat": "09.00-11.00"})
    # c10 = admin.create_course(course_id="5PISA1002", course_name="Artificial Intelligence", instructor="Dr. Kevin", description="Exploring AI algorithms and applications", schedule={"Kamis": "14.00-16.00", "Jumat": "14.00-16.00"})

    # courses = [c1,c2,c3,c4,c5,c6,c7,c8,c9,c10]

    # print(c1)
    # print(c2)
    
    # # assign the lecturer
    # admin.assign_professor(courses, professor)
    # admin.assign_professor(courses, professor1)

    # add course to krs
    # admin.add_course_krs(courses)

    # show krs list 
    # KRS.show_krs("krS5")

    # semester
    # admin.update_semester(student1, 5)
    # print(student.semester)

    # determine krs
    # KRS.determine_krs(student1,"non-paket")
    # student1.view_courses()
    # print(student1.krs)

    # # join course test
    # student.join_course("1SIWP1001", courses)
    # student1.join_course("1SIWP2005", courses)
    # student1.join_course("1SIWP1001", courses)
    # student1.join_course("1SIWP2015" , courses)
    # student1.join_course("",courses)

    # # check the students inside of the course
    # c1.get_student_list()

    # # professor grading
    # professor.post_grade("PEmbelajaraan OOP", student1._name, 90)
    # professor1.post_grade("algoritma", student1._name, 100)

    # # student view grade
    # student1.view_grades()
    # student.view_grades()

    # # professor post attendance
    # professor.post_attendance("pembelajaraan oop", student1._name, "absent")
    # professor1.post_attendance("algoritma", student1._name, "absent")

    # # student view attendance
    # student1.view_attendance()

    # student view courses
    # student1.view_courses()

    # professor post exam schedule
    # professor.post_exam_schedule("pembelajaraan oop", "32 December 2024")
    # professor1.post_exam_schedule("algoritma", "30 December 2024")

    # student view exam schedule
    # student1.view_exam_schedule()

    # # professor post material
    # professor.post_course_material("pembelajaraan oop", "Array in Python")
    # professor.post_course_material("pembelajaraan oop", "Function in Python")
    # professor.post_course_material("pembelajaraan oop", "Conditional Statement in Python")
    # professor1.post_course_material("algoritma", "Matrix")


    # student view material
    # student1.view_course_materials()

    # admin input billing
    # admin.input_billing(student1, 10000000)
    
    # student view billing
    # student1.view_billing()

    # student sumbit certificate
    # student.submit_certificate("Certificate1", "Menang lomba")
    # student.submit_certificate("Certificate1", "a")
    
    # eticket system
    # et_system = ETicketSystem()
    # student1.report_issue("There's a bug in the system.", et_system)
    # admin.view_tickets(et_system)

    # announcement system
    # announce_system = announcementSystem()
    # admin.post_announcement("Hello World", announce_system)
    # admin.post_announcement("Hello World", announce_system)
    # admin.post_announcement("Hello World", announce_system)
    # student.view_announcement(announce_system)

    # library system
    # book1 = Book("Harry Potter and the Philosopher's Stone", "J.K. Rowling", "Fantasy", "Harry found the philosopher stone!")
    # book2 = Book("The Hobbit", "J.R.R. Tolkien", "Fantasy",)
    # book3 = Book("1984", "George Orwell", "Dystopian")
    # books = [book1,book2,book3]
    
    # libraryUKRIDA = Library()
    # librarian.add_books(books, libraryUKRIDA)
    # student.search_books("a", libraryUKRIDA)

    # # student.view_book_content("The Matrix", libraryUKRIDA)
    # student.view_book_content("the hobbit", libraryUKRIDA)

    # librarian.borrow_book("peter","1984")
    # librarian.return_book("peter","The hobbit")

    # backlog
    # admin.clear_backlog()
    


if __name__ == "__main__":
    main()
