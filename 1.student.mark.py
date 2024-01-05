def input_info(prompt, is_float=False):
    return float(input(prompt)) if is_float else input(prompt)

def input_students():
    return {input_info("Enter student ID: "): (input_info("Enter student name: "), input_info("Enter student DoB (dd/mm/yyyy): ")) for _ in range(int(input_info("Enter the number of students in the class: ")))}

def input_courses():
    return {input_info("Enter course ID: "): input_info("Enter course name: ") for _ in range(int(input_info("Enter the number of courses: ")))}

def select_course(courses):
    print("Courses:")
    [print(f"ID: {course_id}, Name: {course_name}") for course_id, course_name in courses.items()]
    return input_info("Select a course by ID to input marks: ")

def input_marks(students, course_id):
    print(f"Entering marks for students in course {course_id}.")
    return {student_id: float(input_info(f"Enter mark for student ID {student_id}, {student[0]}: ")) for student_id, student in students.items()}

def list_items(items, title):
    print(f"{title}:")
    [print(f"ID: {item_id}, {title[:-1]}: {item_name}") for item_id, item_name in items.items()]

def show_marks(course_marks, students, course_id):
    print(f"Marks for course ID {course_id}:")
    [print(f"Student ID: {student_id}, Name: {student[0]}, Mark: {mark}") for student_id, (student, mark) in zip(students.items(), course_marks.items())]

def main():
    students = input_students()
    courses = input_courses()

    course_marks = {}
    while True:
        course_id = select_course(courses)
        course_marks[course_id] = input_marks(students, course_id)

        list_items(students, "Students")
        show_marks(course_marks[course_id], students, course_id)

        if input_info("Would you like to enter marks for another course? (yes/no)") == "no":
            break

    [show_marks(course_marks[course_id], students, course_id) for course_id in course_marks]

if __name__ == "__main__":
    main()
