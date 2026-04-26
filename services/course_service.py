from utils.data_store import courses

def show_courses():
    print("\nCourses:")
    for c in courses.values():
        print(f"{c.cid} | {c.title} | Seats Left: {c.capacity - c.enrolled}")