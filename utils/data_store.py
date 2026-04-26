from models.course import Course

students = {}

courses = {
    "C101": Course("C101", "Maths", 3, ("Mon", "10AM"), 2, []),
    "C102": Course("C102", "Physics", 3, ("Mon", "10AM"), 2, ["C101"]),
    "C103": Course("C103", "Programming", 4, ("Tue", "11AM"), 2, [])
}