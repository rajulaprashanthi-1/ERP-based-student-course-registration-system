class Student:
    def __init__(self, sid, name, program):
        self.sid = sid
        self.name = name
        self.program = program
        self.completed = set()
        self.registered = []
        self.credits = 0