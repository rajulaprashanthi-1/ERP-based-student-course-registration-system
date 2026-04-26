class Course:
    def __init__(self, cid, title, credits, schedule, capacity, prereq):
        self.cid = cid
        self.title = title
        self.credits = credits
        self.schedule = schedule
        self.capacity = capacity
        self.enrolled = 0
        self.prereq = set(prereq)