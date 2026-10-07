import curses

def get_input(stdscr, prompt):
    stdscr.clear()
    stdscr.addstr(2, 2, prompt)
    stdscr.refresh()
    curses.echo()
    val = stdscr.getstr(3, 2).decode('utf-8')
    curses.noecho()
    return val

def input_students():
    students = []
    num_students = int(input("Enter number of students: "))
    
    with open("students.txt", "w") as f:
        for _ in range(num_students):
            student_id = input("Student ID: ")
            name = input("Student Name: ")
            dob = input("Date of Birth (DoB): ")
            
            f.write(f"{student_id},{name},{dob}\n")
            students.append({"id": student_id, "name": name, "dob": dob})
            
    return students


def input_courses():
    courses = []
    num_courses = int(input("Enter number of courses: "))
    
    with open("courses.txt", "w") as f:
        for _ in range(num_courses):
            course_id = input("Course ID: ")
            title = input("Course Title: ")
            credits = input("Credits: ")
            
            f.write(f"{course_id},{title},{credits}\n")
            courses.append({"id": course_id, "title": title, "credits": credits})
            
    return courses


def input_marks(students, course_id):
    marks = {}
    
    # Mode 'a' appends marks so multiple courses don't overwrite previous ones
    with open("marks.txt", "a") as f:
        print(f"\n--- Entering marks for course {course_id} ---")
        for student in students:
            mark = float(input(f"Enter mark for {student['name']} ({student['id']}): "))
            marks[student['id']] = mark
            
            f.write(f"{course_id},{student['id']},{mark}\n")
            
    return marks
