# Input number of students in the class
num_students = int(input("Enter number of students in class: "))

# Input student information: id, name, DoB
students = []
for i in range(num_students):
    student_id = input(f"Enter ID for student {i+1}: ")
    student_name = input(f"Enter name for student {i+1}: ")
    student_dob = input(f"Enter date of birth (DD/MM/YYYY) for student {i+1}: ")
    student = {"id": student_id, "name": student_name, "dob": student_dob}
    students.append(student)

# Input number of courses
num_courses = int(input("Enter the number of courses: "))

# Input course information: id, name
courses = []
for i in range(num_courses):
    course_id = input(f"Enter ID for course {i+1}: ")
    course_name = input(f"Enter name for course {i+1}: ")
    course = {"id": course_id, "name": course_name}
    courses.append(course)

# Select a course, input marks for students in this course
selected_course_id = input("Enter ID of the course you want to input marks for: ")
for course in courses:
    if course["id"] == selected_course_id:
        selected_course = course
        break
if not selected_course:
    print("Invalid course ID")
else:
    for student in students:
        marks = float(input(f"Enter marks for {student['name']} in {selected_course['name']}: "))
        student[selected_course_id] = marks

# Print the student and course information with marks
print("Student information with marks:")
for student in students:
    print(f"ID: {student['id']}, Name: {student['name']}, DoB: {student['dob']}")
    for course in courses:
        if course["id"] in student:
            print(f"  {course['name']}: {student[course['id']]}")