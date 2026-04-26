from utils.data_store import courses

def register_course(student):
    cid = input("Enter Course ID: ")

    if cid not in courses:
        print("Invalid Course")
        return

    course = courses[cid]

    if not course.prereq.issubset(student.completed):
        print("Prerequisites not satisfied")
        return

    if course.enrolled >= course.capacity:
        print("No seats available")
        return

    for c in student.registered:
        if c.schedule == course.schedule:
            print("Time clash!")
            return

    student.registered.append(course)
    student.credits += course.credits
    course.enrolled += 1

    print("Registered successfully!")


def drop_course(student):
    cid = input("Enter Course ID: ")

    for c in student.registered:
        if c.cid == cid:
            student.registered.remove(c)
            student.credits -= c.credits
            c.enrolled -= 1
            print("Course dropped")
            return

    print("Not registered in this course")