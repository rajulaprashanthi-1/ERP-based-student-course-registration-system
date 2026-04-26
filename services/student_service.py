from models.student import Student
from utils.data_store import students

def create_student():
    while True:
        sid = input("Enter Student ID: ")
        if sid in students:
            print("ID already exists!")
        else:
            break

    name = input("Enter Name: ")
    program = input("Enter Program: ")

    s = Student(sid, name, program)

    completed = input("Completed courses (comma separated or blank): ")
    if completed:
        s.completed = set(completed.split(","))

    students[sid] = s
    print("Student created successfully!")
    return s


def select_student():
    while True:
        print("\n1. Login\n2. Create New Student")
        ch = input("Choice: ")

        if ch == '1':
            sid = input("Enter Student ID: ")
            if sid in students:
                return students[sid]
            else:
                print("Student not found!")

        elif ch == '2':
            return create_student()

        else:
            print("Invalid choice!")