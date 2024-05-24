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
    .stMultiselect>div>div>div>label>div {
        color: #333 !important;
        font-size: 16px !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

class Student:
    def __init__(self, name):
        self.name = name
        self.schedule = []

    def add_class(self, course, professor, location, time):
        self.schedule.append({"course": course, "professor": professor, "location": location, "time": time, "homework": []})

    def add_homework(self, course_index, homework):
        if course_index < len(self.schedule):
            self.schedule[course_index]["homework"].append(homework)
        else:
            st.warning("Invalid class index.")

    def remove_homework(self, course_index, homework_index):
        try:
            del self.schedule[course_index]["homework"][homework_index]
        except IndexError:
            st.warning("Homework not found.")
        else:
            st.success("Homework removed successfully.")

    def display_schedule(self):
        for class_info in self.schedule:
            st.write(f"Class: {class_info['course']}")
            st.write(f"Professor: {class_info['professor']}")
            st.write(f"Location: {class_info['location']}")
            st.write(f"Time: {class_info['time']}")
            if class_info["homework"]:
                st.write("Homework Assignments:")
                for j, hw in enumerate(class_info["homework"], start=1):
                    hw_text = f"{j}. {hw}"
                    if st.checkbox(hw_text):
                        st.remove(hw_text)
            else:
                st.write("No homework assigned")

def main():
    st.markdown("# StudentTrack")

    student_name = st.text_input("Enter your name:")
    course = st.text_input("Course:")
    professor = st.text_input("Professor:")
    location = st.text_input("Location:")
    time = st.text_input("Time:")

    student = st.session_state.get('student', None)

    if student is None:
        student = Student(student_name)
        st.session_state['student'] = student

    if st.button("Add Class"):
        student.add_class(course, professor, location, time)
        st.success("Class added successfully!")

    if st.button("View Schedule"):
        if student.schedule:
            student.display_schedule()
        else:
            st.warning("No schedule found.")

    st.markdown("## Add Homework Assignment")
    if student.schedule:
        selected_classes = st.multiselect("Select Classes:", [class_info["course"] for class_info in student.schedule])
        homework = st.text_input("Enter Homework Assignment:")
        if st.button("Add Homework"):
            if selected_classes:
                selected_indices = [i for i, class_info in enumerate(student.schedule) if class_info["course"] in selected_classes]
                for index in selected_indices:
                    student.add_homework(index, homework)
                st.success("Homework added successfully!")
            else:
                st.warning("Please select at least one class.")

    if st.button("Remove Finished Homework"):
        if student.schedule:
            selected_classes = st.multiselect("Select Classes:", [class_info["course"] for class_info in student.schedule])
            if selected_classes:
                selected_course_index = [i for i, class_info in enumerate(student.schedule) if class_info["course"] in selected_classes][0]
                if student.schedule[selected_course_index]["homework"]:
                    selected_homework_index = st.selectbox("Select Homework Assignment:",
                                                           [hw for hw in student.schedule[selected_course_index]["homework"]])
                    student.remove_homework(selected_course_index, student.schedule[selected_course_index]["homework"].index(selected_homework_index))
                    st.success("Homework removed successfully!")
                else:
                    st.warning("No homework assigned for selected class.")
            else:
                st.warning("Please select at least one class.")

if __name__ == "__main__":
    main()
