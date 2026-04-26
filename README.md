Section No: 10
Project Title: ERP-based-student-course-registration-system
Team Member IDs:
2500032658
2500032734
2500032743
2500040015

*ERP-Based Student Course Registration System

*Project Overview

This project is a Python-based ERP (Enterprise Resource Planning) system designed to manage student course registration efficiently. It simulates real-world university systems by handling student data, course enrollment, prerequisite validation, and analytics.

-Features

*Student Management

 > Create new student profiles
 > Login using Student ID
 > Track completed and registered courses

* Course Management

> View available courses
> Check seat availability
> Course details (credits, schedule, prerequisites)

* Registration System

> Register for courses
> Drop courses
> Automatic prerequisite checking
> Seat capacity validation
> Timetable clash detection

* Analytics

> Average credits calculation using NumPy
> Course enrollment statistics using Pandas
> Graphical representation using Matplotlib


* Technologies Used

> Python 
> Pandas 
> NumPy 
> Matplotlib 


* Project Structure

ERPSystem
──> main.py
──> models
     ──> student.py
     ──> course.py
──> services
     ──> student_service.py
     ──> course_service.py
     ──> registration_service.py
──> utils
     ──> analytics.py  
     

* How to Run the Project

1. Install required libraries:

pip install pandas numpy matplotlib

2. Run the program:

python main.py


- Sample Usage

* Create a new student
* Login with Student ID
* View available courses
* Register for courses (C101, C102, C103)
* View analytics (graph will be displayed)


* Example Courses

| Course ID | Name        | Credits | Prerequisite |
| --------- | ----------- | ------- | ------------ |
| C101      | Maths       | 3       | None         |
| C102      | Physics     | 3       | C101         |
| C103      | Programming | 4       | None         |


- Learning Outcomes

* Understanding ERP system design
* Applying Object-Oriented Programming (OOP)
* Working with real-world data using Pandas
* Data visualization using Matplotlib
* Modular programming in Python


- Future Enhancements

* Database integration (MySQL / SQLite)
* GUI interface (Tkinter / Web App)
* User authentication with passwords
* Auto-generated student IDs
* Online course portal
