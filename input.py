import curses

def get_input(stdscr, prompt):
    """Helper to prompt and get string input from user in curses."""
    stdscr.clear()
    stdscr.addstr(2, 2, prompt)
    stdscr.refresh()
    curses.echo()
    val = stdscr.getstr(3, 2).decode('utf-8')
    curses.noecho()
    return val

def input_students(stdscr, system):
    num = int(get_input(stdscr, "Enter number of students: "))
    for i in range(num):
        s_id = get_input(stdscr, f"Student {i+1} ID: ")
        name = get_input(stdscr, f"Student {i+1} Name: ")
        dob = get_input(stdscr, f"Student {i+1} DoB (DD/MM/YYYY): ")
        system.add_student(s_id, name, dob)

def input_courses(stdscr, system):
    num = int(get_input(stdscr, "Enter number of courses: "))
    for i in range(num):
        c_id = get_input(stdscr, f"Course {i+1} ID: ")
        name = get_input(stdscr, f"Course {i+1} Name: ")
        credits = int(get_input(stdscr, f"Course {i+1} Credits: "))
        system.add_course(c_id, name, credits)

def input_marks(stdscr, system):
    c_id = get_input(stdscr, "Enter Course ID to input marks for: ")
    students = system.get_students()
    for s in students:
        raw_m = float(get_input(stdscr, f"Mark for {s.get_name()} ({s.get_id()}): "))
        system.add_mark(c_id, s.get_id(), raw_m)