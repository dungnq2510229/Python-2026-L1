import curses
from domains.mark_management import MarkManagementSystem
from input import get_input
from output import draw_menu, display_courses, display_students, display_marks

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
            display_courses(stdscr, system.get_courses())

        elif ch == '5':
            system.sort_students_by_gpa()
            display_students(stdscr, system.get_students())

        elif ch == '6':
            c_id = get_input(stdscr, "Enter Course ID to show marks: ")
            marks = system.get_marks(c_id)
            display_marks(stdscr, c_id, system.get_students(), marks)

        elif ch == '7':
            break

def main():
    system = MarkManagementSystem()
    curses.wrapper(run_app, system)

if __name__ == "__main__":
    main()