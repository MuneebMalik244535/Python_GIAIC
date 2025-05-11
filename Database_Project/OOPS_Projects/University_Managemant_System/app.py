
import streamlit as st
import firebase_admin
from firebase_admin import credentials
import json
# Firebase credentials load from Streamlit secrets
cred = credentials.Certificate(dict(st.secrets["FIREBASE"]))

# Initialize Firebase
firebase_admin.initialize_app(cred)



# # Initialize Firebase only once
# if not firebase_admin._apps:
#     cred = credentials.Certificate("firebase_key.json")
#     firebase_admin.initialize_app(cred)

db = firestore.client()

# --- Classes ---
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Instructor(Person):
    def __init__(self, name, age, salary, courses=None):
        super().__init__(name, age)
        self.salary = salary
        self.courses = courses if courses else []

class Student(Person):
    def __init__(self, name, age, enrolled_courses=None):
        super().__init__(name, age)
        self.enrolled_courses = enrolled_courses if enrolled_courses else []

class Course:
    def __init__(self, name, instructor=None, students=None):
        self.name = name
        self.instructor = instructor
        self.students = students if students else []

# --- Firestore Functions ---
def save_student_to_firestore(student):
    db.collection("students").add({
        "name": student.name,
        "age": student.age,
        "enrolled_courses": student.enrolled_courses
    })

def save_instructor_to_firestore(instructor):
    db.collection("instructors").add({
        "name": instructor.name,
        "age": instructor.age,
        "salary": instructor.salary,
        "courses": instructor.courses
    })

def save_course_to_firestore(course):
    db.collection("courses").add({
        "name": course.name,
        "instructor": course.instructor if course.instructor else None,
        "students": course.students
    })

def get_all_students():
    return [Student(doc.to_dict()['name'], doc.to_dict()['age'], doc.to_dict().get('enrolled_courses', [])) for doc in db.collection("students").stream()]

def get_all_instructors():
    return [Instructor(doc.to_dict()['name'], doc.to_dict()['age'], doc.to_dict()['salary'], doc.to_dict().get('courses', [])) for doc in db.collection("instructors").stream()]

def get_all_courses():
    return [Course(doc.to_dict()['name'], doc.to_dict().get('instructor'), doc.to_dict().get('students', [])) for doc in db.collection("courses").stream()]

# --- Streamlit UI ---
st.title("🎓 University Management System")

menu = st.sidebar.selectbox("Select Option", [
    "Add Student", "Add Instructor", "Add Course",
    "Assign Instructor to Course", "Enroll Student in Course",
    "Show All Students", "Show All Instructors", "Show All Courses"
])

if menu == "Add Student":
    st.subheader("➕ Add Student")
    name = st.text_input("Name")
    age = st.number_input("Age", min_value=1, step=1)
    if st.button("Add Student"):
        student = Student(name, int(age))
        save_student_to_firestore(student)
        st.success("✅ Student added.")

elif menu == "Add Instructor":
    st.subheader("➕ Add Instructor")
    name = st.text_input("Name")
    age = st.number_input("Age", min_value=1, step=1)
    salary = st.number_input("Salary", min_value=0.0, step=100.0)
    if st.button("Add Instructor"):
        instructor = Instructor(name, int(age), float(salary))
        save_instructor_to_firestore(instructor)
        st.success("✅ Instructor added.")

elif menu == "Add Course":
    st.subheader("➕ Add Course")
    name = st.text_input("Course Name")
    if st.button("Add Course"):
        course = Course(name)
        save_course_to_firestore(course)
        st.success("✅ Course added.")

elif menu == "Assign Instructor to Course":
    st.subheader("📘 Assign Instructor to Course")
    courses = get_all_courses()
    instructors = get_all_instructors()
    if not courses or not instructors:
        st.warning("⚠️ Please make sure both instructors and courses exist.")
    else:
        course_names = [c.name for c in courses]
        instructor_names = [i.name for i in instructors]
        selected_course = st.selectbox("Select Course", course_names)
        selected_instructor = st.selectbox("Select Instructor", instructor_names)

        if st.button("Assign"):
            # update course and instructor
            db_courses = db.collection("courses").where("name", "==", selected_course).get()
            for doc in db_courses:
                db.collection("courses").document(doc.id).update({"instructor": selected_instructor})

            db_instructors = db.collection("instructors").where("name", "==", selected_instructor).get()
            for doc in db_instructors:
                instructor_data = doc.to_dict()
                courses_list = instructor_data.get("courses", [])
                if selected_course not in courses_list:
                    courses_list.append(selected_course)
                db.collection("instructors").document(doc.id).update({"courses": courses_list})

            st.success("✅ Instructor assigned to course.")

elif menu == "Enroll Student in Course":
    st.subheader("📘 Enroll Student in Course")
    courses = get_all_courses()
    students = get_all_students()
    if not courses or not students:
        st.warning("⚠️ Please make sure both students and courses exist.")
    else:
        course_names = [c.name for c in courses]
        student_names = [s.name for s in students]
        selected_course = st.selectbox("Select Course", course_names)
        selected_student = st.selectbox("Select Student", student_names)

        if st.button("Enroll"):
            # update course and student
            db_courses = db.collection("courses").where("name", "==", selected_course).get()
            for doc in db_courses:
                course_data = doc.to_dict()
                student_list = course_data.get("students", [])
                if selected_student not in student_list:
                    student_list.append(selected_student)
                db.collection("courses").document(doc.id).update({"students": student_list})

            db_students = db.collection("students").where("name", "==", selected_student).get()
            for doc in db_students:
                student_data = doc.to_dict()
                enrolled_list = student_data.get("enrolled_courses", [])
                if selected_course not in enrolled_list:
                    enrolled_list.append(selected_course)
                db.collection("students").document(doc.id).update({"enrolled_courses": enrolled_list})

            st.success("✅ Student enrolled in course.")

elif menu == "Show All Students":
    st.subheader("📋 All Students")
    students = get_all_students()
    if students:
        for s in students:
            st.text(f"Name: {s.name}, Age: {s.age}, Enrolled: {', '.join(s.enrolled_courses)}")
    else:
        st.info("No students found.")

elif menu == "Show All Instructors":
    st.subheader("📋 All Instructors")
    instructors = get_all_instructors()
    if instructors:
        for i in instructors:
            st.text(f"Name: {i.name}, Age: {i.age}, Salary: {i.salary}, Courses: {', '.join(i.courses)}")
    else:
        st.info("No instructors found.")

elif menu == "Show All Courses":
    st.subheader("📋 All Courses")
    courses = get_all_courses()
    if courses:
        for c in courses:
            st.text(f"Course: {c.name}, Instructor: {c.instructor or 'None'}, Students: {', '.join(c.students)}")
    else:
        st.info("No courses found.")
