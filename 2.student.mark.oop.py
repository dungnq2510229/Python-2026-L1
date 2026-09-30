
# Sorry was burnt out so i don't even understand what i write (With AI Assists) afterward sometime
class Student:
    def __init__(self, student_id="", name="", dob=""):
        # Encapsulation: Private attributes to protect student data
        # More detailed: in Python means restricting direct access to an object's internal data by using naming conventions
        # You don't have to read those complex explainations, just understand we use a bunch of functions instead here
        self.__id = student_id
        self.__name = name
        self.__dob = dob

    # Getters to access private attributes from outside the class
    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def get_dob(self):
        return self.__dob

    # Polymorphism: Shared method name `input()` across domain classes
    # More detailed: Polymorphism in Python means using a single interface (a function for example) to work with different object types
    # , allowing each object to respond in its own way.
    def input(self):
        self.__id = input("ID: ")
        self.__name = input("Name: ")
        self.__dob = input("DoB (DD/MM/YYYY): ")

    # Polymorphism: Shared method name `list()` to display entity details
    def list(self):
        print(f"ID: {self.__id} | Name: {self.__name} | DoB: {self.__dob}")


class Course:
    def __init__(self, course_id="", name=""):
        # Encapsulation: Private attributes for course details
        self.__id = course_id
        self.__name = name

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    # Polymorphism: Same `input()` method name as in Student class
    def input(self):
        self.__id = input("ID: ")
        self.__name = input("Name: ")

    # Polymorphism: Same `list()` method name as in Student class
    def list(self):
        print(f"ID: {self.__id} | Name: {self.__name}")


class MarkManagementSystem:
    def __init__(self):
        # All management data is stored inside instance attributes instead of global variables
        self.__students = []
        self.__courses = []
        # Stores marks structure: {course_id: {student_id: mark_value}}
        self.__marks = {}

    def input_students(self):
        num_students = int(input("Enter number of students in class: "))
        for i in range(num_students):
            print(f"\nStudent {i + 1}")
            s = Student()
            s.input()  # Calls the Student's input method
            self.__students.append(s)

    def input_courses(self):
        num_courses = int(input("Enter number of courses: "))
        for i in range(num_courses):
            print(f"\nCourse {i + 1}")
            c = Course()
            c.input()  # Calls the Course's input method
            self.__courses.append(c)

    def list_students(self):
        print("\n--- Student List ---")
        if not self.__students:
            print("No students available.")
            return
        for s in self.__students:
            s.list()  # Polymorphic method call

    def list_courses(self):
        print("\n--- Course List ---")
        if not self.__courses:
            print("No courses available.")
            return
        for c in self.__courses:
            c.list()  # Polymorphic method call

    def input_marks(self):
        if not self.__courses or not self.__students:
            print("Please enter courses and students first.")
            return

        self.list_courses()
        course_id = input("\nSelect course ID to enter marks for: ")

        # Check if course exists using getter method
        course_exists = any(c.get_id() == course_id for c in self.__courses)
        if not course_exists:
            print("Invalid course ID.")
            return

        if course_id not in self.__marks:
            self.__marks[course_id] = {}

        print(f"\nEnter marks for course ID: {course_id}")
        for s in self.__students:
            mark = float(input(f"Mark for {s.get_name()} (ID: {s.get_id()}): "))
            self.__marks[course_id][s.get_id()] = mark

    def show_student_marks(self):
        if not self.__courses:
            print("No courses available.")
            return

        self.list_courses()
        course_id = input("\nEnter course ID to view marks: ")

        if course_id not in self.__marks or not self.__marks[course_id]:
            print("No marks found for this course.")
            return

        print(f"\n--- Marks for Course {course_id} ---")
        for s in self.__students:
            s_id = s.get_id()
            if s_id in self.__marks[course_id]:
                print(f"ID: {s_id} | Name: {s.get_name()} | Mark: {self.__marks[course_id][s_id]}")


def main():
    # Create a single system controller object
    system = MarkManagementSystem()

    while True:
        print("\n=== STUDENT MARK MANAGEMENT SYSTEM ===")
        print("1. Add Students")
        print("2. Add Courses")
        print("3. Input Marks")
        print("4. List Courses")
        print("5. List Students")
        print("6. Show Marks")
        print("7. Exit")

        choice = input("Select an option (1-7): ")

        if choice == "1":
            system.input_students()
        elif choice == "2":
            system.input_courses()
        elif choice == "3":
            system.input_marks()
        elif choice == "4":
            system.list_courses()
        elif choice == "5":
            system.list_students()
        elif choice == "6":
            system.show_student_marks()
        elif choice == "7":
            print("Exiting program.")
            break
        else:
            print("Invalid selection. Try again.")


if __name__ == "__main__":
    main()