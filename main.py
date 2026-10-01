import curses
from domains.mark_system import MarkManagementSystem
from input import input_students, input_courses, input_marks
from output import draw_menu, list_courses, list_students, show_marks

def run_app(stdscr, system):
    curses.curs_set(1)

    while True:
        draw_menu(stdscr)
        ch = stdscr.getkey()

        if ch == '1':
            input_students(stdscr, system)
        elif ch == '2':
            input_courses(stdscr, system)
        elif ch == '3':
            input_marks(stdscr, system)
        elif ch == '4':
            list_courses(stdscr, system)
        elif ch == '5':
            list_students(stdscr, system)
        elif ch == '6':
            show_marks(stdscr, system)
        elif ch == '7':
            break

def main():
    system = MarkManagementSystem()
    curses.wrapper(run_app, system)

if __name__ == "__main__":
    main()