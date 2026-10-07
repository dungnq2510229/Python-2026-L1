import curses

def draw_menu(stdscr):
    stdscr.clear()
    stdscr.border(0)
    stdscr.addstr(1, 2, "=== STUDENT MARK MANAGEMENT SYSTEM (PW4) ===", curses.A_BOLD)
    stdscr.addstr(3, 4, "1. Add Students")
    stdscr.addstr(4, 4, "2. Add Courses")
    stdscr.addstr(5, 4, "3. Input Marks")
    stdscr.addstr(6, 4, "4. List Courses")
    stdscr.addstr(7, 4, "5. List Students (Sorted by GPA)")
    stdscr.addstr(8, 4, "6. Show Marks for Course")
    stdscr.addstr(9, 4, "7. Exit")
    stdscr.addstr(11, 2, "Select an option (1-7): ")
    stdscr.refresh()

def display_courses(stdscr, courses):
    stdscr.clear()
    stdscr.addstr(1, 2, "--- COURSE LIST ---", curses.A_BOLD)
    row = 3
    for c in courses:
        stdscr.addstr(row, 2, f"ID: {c.get_id()} | Name: {c.get_name()} | Credits: {c.get_credits()}")
        row += 1
    stdscr.addstr(row + 1, 2, "Press any key to return...")
    stdscr.getch()

def display_students(stdscr, students):
    stdscr.clear()
    stdscr.addstr(1, 2, "--- STUDENT LIST (Sorted by GPA Descending) ---", curses.A_BOLD)
    row = 3
    for s in students:
        stdscr.addstr(row, 2, f"ID: {s.get_id()} | Name: {s.get_name()} | DoB: {s.get_dob()} | GPA: {s.get_gpa():.2f}")
        row += 1
    stdscr.addstr(row + 1, 2, "Press any key to return...")
    stdscr.getch()

def display_marks(stdscr, course_id, students, marks):
    stdscr.clear()
    stdscr.addstr(1, 2, f"--- MARKS FOR COURSE: {course_id} ---", curses.A_BOLD)
    row = 3
    for s in students:
        if s.get_id() in marks:
            stdscr.addstr(row, 2, f"ID: {s.get_id()} | Name: {s.get_name()} | Mark: {marks[s.get_id()]}")
            row += 1
    stdscr.addstr(row + 1, 2, "Press any key to return...")
    stdscr.getch()