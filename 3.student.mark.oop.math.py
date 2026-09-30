import math
import curses
import numpy as np


class Student:
    def __init__(self, student_id="", name="", dob=""):
        self.__id = student_id
        self.__name = name
        self.__dob = dob
        self.__gpa = 0.0

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def get_dob(self):
        return self.__dob

    def set_gpa(self, gpa):
        self.__gpa = gpa

    def get_gpa(self):
        return self.__gpa


class Course:
    def __init__(self, course_id="", name="", credits=0):
        self.__id = course_id
        self.__name = name
        self.__credits = credits

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def get_credits(self):
        return self.__credits


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
        # Round down to 1-digit decimal using math.floor
        floored_mark = math.floor(raw_mark * 10) / 10
        if course_id not in self.__marks:
            self.__marks[course_id] = {}
        self.__marks[course_id][student_id] = floored_mark

    def get_marks(self, course_id):
        return self.__marks.get(course_id, {})

    def calculate_gpas(self):
        """Calculates weighted GPA using numpy arrays and updates students."""
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
                # Weighted sum / total credits
                gpa = np.sum(marks_arr * credits_arr) / np.sum(credits_arr)
                s.set_gpa(round(gpa, 2))
            else:
                s.set_gpa(0.0)

    def sort_students_by_gpa(self):
        """Sorts student list descending by GPA."""
        self.calculate_gpas()
        self.__students.sort(key=lambda s: s.get_gpa(), reverse=True)


def get_input(stdscr, prompt):
    """Helper to prompt and get string input from user in curses."""
    stdscr.clear()
    stdscr.addstr(2, 2, prompt)
    stdscr.refresh()
    curses.echo()
    val = stdscr.getstr(3, 2).decode('utf-8')
    curses.noecho()
    return val


def draw_menu(stdscr):
    stdscr.clear()
    stdscr.border(0)
    stdscr.addstr(1, 2, "=== STUDENT MARK MANAGEMENT SYSTEM (PW3) ===", curses.A_BOLD)
    stdscr.addstr(3, 4, "1. Add Students")
    stdscr.addstr(4, 4, "2. Add Courses")
    stdscr.addstr(5, 4, "3. Input Marks")
    stdscr.addstr(6, 4, "4. List Courses")
    stdscr.addstr(7, 4, "5. List Students (Sorted by GPA)")
    stdscr.addstr(8, 4, "6. Show Marks for Course")
    stdscr.addstr(9, 4, "7. Exit")
    stdscr.addstr(11, 2, "Select an option (1-7): ")
    stdscr.refresh()


def run_app(stdscr, system):
    curses.curs_set(1)

    while True:
        draw_menu(stdscr)
        ch = stdscr.getkey()

        if ch == '1':
            num = int(get_input(stdscr, "Enter number of students: "))
            for i in range(num):
                s_id = get_input(stdscr, f"Student {i+1} ID: ")
                name = get_input(stdscr, f"Student {i+1} Name: ")
                dob = get_input(stdscr, f"Student {i+1} DoB (DD/MM/YYYY): ")
                system.add_student(s_id, name, dob)

        elif ch == '2':
            num = int(get_input(stdscr, "Enter number of courses: "))
            for i in range(num):
                c_id = get_input(stdscr, f"Course {i+1} ID: ")
                name = get_input(stdscr, f"Course {i+1} Name: ")
                credits = int(get_input(stdscr, f"Course {i+1} Credits: "))
                system.add_course(c_id, name, credits)

        elif ch == '3':
            c_id = get_input(stdscr, "Enter Course ID to input marks for: ")
            students = system.get_students()
            for s in students:
                raw_m = float(get_input(stdscr, f"Mark for {s.get_name()} ({s.get_id()}): "))
                system.add_mark(c_id, s.get_id(), raw_m)

        elif ch == '4':
            stdscr.clear()
            stdscr.addstr(1, 2, "--- COURSE LIST ---", curses.A_BOLD)
            row = 3
            for c in system.get_courses():
                stdscr.addstr(row, 2, f"ID: {c.get_id()} | Name: {c.get_name()} | Credits: {c.get_credits()}")
                row += 1
            stdscr.addstr(row + 1, 2, "Press any key to return...")
            stdscr.getch()

        elif ch == '5':
            system.sort_students_by_gpa()
            stdscr.clear()
            stdscr.addstr(1, 2, "--- STUDENT LIST (Sorted by GPA Descending) ---", curses.A_BOLD)
            row = 3
            for s in system.get_students():
                stdscr.addstr(row, 2, f"ID: {s.get_id()} | Name: {s.get_name()} | DoB: {s.get_dob()} | GPA: {s.get_gpa():.2f}")
                row += 1
            stdscr.addstr(row + 1, 2, "Press any key to return...")
            stdscr.getch()

        elif ch == '6':
            c_id = get_input(stdscr, "Enter Course ID to show marks: ")
            marks = system.get_marks(c_id)
            stdscr.clear()
            stdscr.addstr(1, 2, f"--- MARKS FOR COURSE: {c_id} ---", curses.A_BOLD)
            row = 3
            for s in system.get_students():
                if s.get_id() in marks:
                    stdscr.addstr(row, 2, f"ID: {s.get_id()} | Name: {s.get_name()} | Mark: {marks[s.get_id()]}")
                    row += 1
            stdscr.addstr(row + 1, 2, "Press any key to return...")
            stdscr.getch()

        elif ch == '7':
            break


def main():
    system = MarkManagementSystem()
    curses.wrapper(run_app, system)


if __name__ == "__main__":
    main()

# Have to run it in an older version of Python, in git bash, with downloading curses and numpy manually for 3.12 there.
# Because VS codes keep giving error as "import curse" does not work.