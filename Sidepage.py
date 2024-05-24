import streamlit as st

# Define custom CSS styles
st.markdown(
    """
    <style>
    .stTextInput>div>div>input {
        background-color: #f0f0f0 !important;
        color: #333 !important;
        font-size: 16px !important;
        border-radius: 5px !important;
    }
    .stButton>button {
        background-color: #007bff !important;
        color: #fff !important;
        font-size: 18px !important;
        font-weight: bold !important;
        padding: 10px 20px !important;
        border-radius: 5px !important;
    }
    .stMarkdown>div>div {
        color: #007bff !important;
        font-size: 24px !important;
        font-weight: bold !important;
        padding-bottom: 20px !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

class Student:
    def __init__(self, name):
        self.name = name
        self.classes = {}

    def add_class(self, course):
        self.classes[course] = []

    def add_homework(self, course, homework):
        if course in self.classes:
            self.classes[course].append(homework)
        else:
            st.error(f"Class '{course}' not found.")

def main():
    st.markdown("# Homework Tracker")

    student_name = st.text_input("Enter your name:")
    course = st.text_input("Course:")

    student = st.session_state.get('student', None)

    if student is None:
        student = Student(student_name)
        st.session_state['student'] = student

    if st.button("Add Class"):
        student.add_class(course)
        st.success("Class added successfully!")

    homework = st.text_input("Enter Homework Assignment:")
    if st.button("Add Homework"):
        student.add_homework(course, homework)
        st.success("Homework added successfully!")

if __name__ == "__main__":
    main()
