class KRS:
    krs1 = []
    krs2 = []
    krs3 = []
    krs4 = []
    krs5 = []

    @staticmethod
    def determine_krs(student, package):
        if package == "non-paket":
            print(f'Student {student._name} can pick their own courses.')
        elif package == "paket":
            if student.semester < 6:
                if student.semester == 1:
                    student.course_list.append(KRS.krs1)
                elif student.semester == 2:
                    student.course_list.append(KRS.krs2)
                elif student.semester == 3:
                    student.course_list.append(KRS.krs3)
                elif student.semester == 4:
                    student.course_list.append(KRS.krs4)
                else:
                    student.course_list.append(KRS.krs5)         
                student.krs = "paket"       
            else:
                print(f'Student {student._name} is not eligible for the "paket" option, please choose the "non-paket" option')
        else:
            print("Invalid package type. Please choose either 'non-paket' or 'paket'.")
    
    def show_krs(krs):
        if krs.lower() == "krs1":
            if not KRS.krs1:
                print("No courses in KRS1")
            else:
                print("Courses in KRS1:")
                for course in KRS.krs1:
                    print(course)
        elif krs.lower() == "krs2":
            if not KRS.krs2:
                print("No courses in KRS2")
            else:
                print("Courses in KRS2:")
                for course in KRS.krs2:
                    print(course)
        elif krs.lower() == "krs3":
            if not KRS.krs3:
                print("No courses in KRS3")
            else:
                print("Courses in KRS3:")
                for course in KRS.krs3:
                    print(course)
        elif krs.lower() == "krs4":
            if not KRS.krs4:
                print("No courses in KRS4")
            else:
                print("Courses in KRS4:")
                for course in KRS.krs4:
                    print(course)
        elif krs.lower() == "krs5":
            if not KRS.krs5:
                print("No courses in KRS5")
            else:
                print("Courses in KRS5:")
                for course in KRS.krs5:
                    print(course)
        else:
            print('Available KRS = krs1 to krs5')

