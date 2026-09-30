#global variables

students = []
courses = []
marks = {}

#input

def input_students():
    num_students = int(input("Enter number of students in class: "))
    for i in range(num_students):
        print(f"\n Student {i + 1} ")
        student_id = input("ID: ")
        name = input("Name: ")
        dob = input("DoB (DD/MM/YYYY): ")
        students.append({"id": student_id, "name": name, "dob": dob})

def input_courses():
    num_courses = int(input("Enter number of courses: "))
    for i in range(num_courses):
        print(f"\n Course {i + 1} ")
        course_id = input("ID: ")
        name = input("Name: ")
        courses.append({"id": course_id, "name": name})


def input_marks():
    if not courses or not students:
        print("Please enter courses and students first:")
        return
    
#listing

    list_courses()
    course_id = input("\nSelect course ID to enter marks for: ")

    course_exists = any(c["id"] == course_id for c in courses)
    if not course_exists:
        print("Invalid course ID")
        return

    if course_id not in marks:
        marks[course_id] = {}

    print(f"\nEnter marks for course: {course_id}:")
    for student in students:
        mark = float(
            input(f"Mark for {student['name']} (ID: {student['id']}): ")
        )
        marks[course_id][student["id"]] = mark


def list_courses():
    print("\n Course List ")
    if not courses:
        print("No courses available")
        return
    
    for c in courses:
        print(f"ID: {c['id']} | Name: {c['name']}")


def list_students():
    print("\n Student List ")
    if not students:
        print("No students available")
        return
    
    for s in students:
        print(f"ID: {s['id']} | Name: {s['name']} | DoB: {s['dob']}")


def show_student_marks():
    if not courses:
        print("No courses available.")
        return

    list_courses()
    course_id = input("\nEnter course ID to view marks: ")

    if course_id not in marks or not marks[course_id]:
        print("No marks found for this course.")
        return

    print(f"\n Marks for Course {course_id} c")
    for student in students:
        s_id = student["id"]
        if s_id in marks[course_id]:
            print(f"ID: {s_id} | Name: {student['name']} | Mark: {marks[course_id][s_id]}")

#control flow and execution

def main():
    while True:
        print(" STUDENT MARK MANAGEMENT SYSTEM")
        print("1. Students")
        print("2. Courses")
        print("3. Marks")
        print("4. List Courses")
        print("5. List Students")
        print("6. List Marks")
        print("7. Get away from this place")

        choice = input("Select an option (1-7): ")

        if choice == "1":
            input_students()
        elif choice == "2":
            input_courses()
        elif choice == "3":
            input_marks()
        elif choice == "4":
            list_courses()
        elif choice == "5":
            list_students()
        elif choice == "6":
            show_student_marks()
        elif choice == "7":
            print("Exiting program.")
            break
        else:
            print("Invalid selection. Try again.")


if __name__ == "__main__":
    main()