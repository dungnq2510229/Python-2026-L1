import math
import numpy as np
from domains.student import Student
from domains.course import Course

class MarkManagementSystem:
    def __init__(self):
        self.__students = []
        self.__courses = []
        self.__marks = {}  # {course_id: {student_id: mark}}

    def add_student(self, student_id, name, dob):
        self.__students.append(Student(student_id, name, dob))

    def add_course(self, course_id, name, credits):
        self.__courses.append(Course(course_id, name, credits))

    def get_students(self):
        return self.__students

    def get_courses(self):
        return self.__courses

    def add_mark(self, course_id, student_id, raw_mark):
        floored_mark = math.floor(raw_mark * 10) / 10
        if course_id not in self.__marks:
            self.__marks[course_id] = {}
        self.__marks[course_id][student_id] = floored_mark

    def get_marks(self, course_id):
        return self.__marks.get(course_id, {})

    def calculate_gpas(self):
        for s in self.__students:
            s_id = s.get_id()
            student_marks = []
            course_credits = []

            for c in self.__courses:
                c_id = c.get_id()
                if c_id in self.__marks and s_id in self.__marks[c_id]:
                    student_marks.append(self.__marks[c_id][s_id])
                    course_credits.append(c.get_credits())

            if course_credits:
                marks_arr = np.array(student_marks)
                credits_arr = np.array(course_credits)
                gpa = np.sum(marks_arr * credits_arr) / np.sum(credits_arr)
                s.set_gpa(round(gpa, 2))
            else:
                s.set_gpa(0.0)

    def sort_students_by_gpa(self):
        self.calculate_gpas()
        self.__students.sort(key=lambda s: s.get_gpa(), reverse=True)