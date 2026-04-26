from services.student_service import select_student
from services.course_service import show_courses
from services.registration_service import register_course, drop_course
from services.analytics_service import analytics

def main():
    print("===== ERP COURSE SYSTEM =====")

    student = select_student()
    print("Welcome", student.name)

    while True:
        print("\n1.View Courses\n2.Register\n3.Drop\n4.Analytics\n5.Switch Student\n6.Exit")
        ch = input("Choice: ")

        if ch == '1':
            show_courses()

        elif ch == '2':
            register_course(student)

        elif ch == '3':
            drop_course(student)

        elif ch == '4':
            analytics()

        elif ch == '5':
            student = select_student()
            print("Switched to", student.name)

        elif ch == '6':
            print("Exiting safely...")
            break

        else:
            print("Invalid choice! Try again.")

if __name__ == "__main__":
    main()