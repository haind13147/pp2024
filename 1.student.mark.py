def input_number_of_students():
    return int(input("Enter the number of students in the class: "))

def input_student_info():
    students = {}
    num_students = input_number_of_students()
    for _ in range(num_students):
        student_id = input("Enter student ID: ")
        student_name = input("Enter student name: ")
        student_dob = input("Enter student DoB (dd/mm/yyyy): ")
        students[student_id] = (student_name, student_dob)
    return students

def input_number_of_courses():
    return int(input("Enter the number of courses: "))

def input_course_info():
    courses = {}
    num_courses = input_number_of_courses()
    for _ in range(num_courses):
        course_id = input("Enter course ID: ")
        course_name = input("Enter course name: ")
        courses[course_id] = course_name
    return courses

def select_course(courses):
    list_courses(courses)
    course_id = input("Select a course by ID to input marks: ")
    return course_id

def input_marks_for_students_in_course(students, course_id):
    print(f"Entering marks for students in course {course_id}.")
    marks = {}
    for student_id in students:
        mark = float(input(f"Enter mark for student ID {student_id}, {students[student_id][0]}: "))
        marks[student_id] = mark
    return marks

def list_courses(courses):
    print("Courses:")
    for course_id, course_name in courses.items():
        print(f"ID: {course_id}, Name: {course_name}")

def list_students(students):
    print("Students:")
    for student_id, (student_name, student_dob) in students.items():
        print(f"ID: {student_id}, Name: {student_name}, DoB: {student_dob}")

def show_student_marks_for_course(course_marks, students, course_id):
    print(f"Marks for course ID {course_id}:")
    for student_id, mark in course_marks.items():
        print(f"Student ID: {student_id}, Name: {students[student_id][0]}, Mark: {mark}")

def main():
    students = input_student_info()
    courses = input_course_info()

    course_marks = {}
    while True:
        course_id = select_course(courses)
        course_marks[course_id] = input_marks_for_students_in_course(students, course_id)

        list_students(students)
        show_student_marks_for_course(course_marks[course_id], students, course_id)

        if input("Would you like to enter marks for another course? (yes/no) ") == "no":
            break

    for course_id in course_marks:
        show_student_marks_for_course(course_marks[course_id], students, course_id)

if __name__ == "__main__":
    main()