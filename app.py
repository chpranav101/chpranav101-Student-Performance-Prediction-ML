import streamlit as st
import pickle
import pandas as pd

# Load model
model = pickle.load(open("student_performance_model.pkl", "rb"))

# Load feature names
feature_columns = pickle.load(open("feature_columns.pkl", "rb"))

st.title("🎓 Student Performance Prediction")
st.write("Enter the student's details below to predict the final grade.")

study_hours = st.number_input("Study Hours", min_value=0, max_value=24, value=5)
attendance = st.number_input("Attendance", min_value=0, max_value=100, value=80)
resources = st.number_input("Resources", min_value=0, max_value=10, value=5)
extracurricular = st.number_input("Extracurricular", min_value=0, max_value=1, value=1)
motivation = st.number_input("Motivation", min_value=0, max_value=10, value=7)
internet = st.number_input("Internet", min_value=0, max_value=1, value=1)
gender = st.number_input("Gender (0=Female, 1=Male)", min_value=0, max_value=1, value=1)
age = st.number_input("Age", min_value=15, max_value=30, value=20)
learning_style = st.number_input("Learning Style", min_value=0, max_value=3, value=1)
online_courses = st.number_input("Online Courses", min_value=0, max_value=10, value=3)
discussions = st.number_input("Discussions", min_value=0, max_value=10, value=5)
assignment_completion = st.number_input("Assignment Completion", min_value=0, max_value=10, value=8)
edutech = st.number_input("EduTech", min_value=0, max_value=1, value=1)
stress_level = st.number_input("Stress Level", min_value=0, max_value=10, value=3)

if st.button("Predict Final Grade"):

    input_data = pd.DataFrame([[
        study_hours,
        attendance,
        resources,
        extracurricular,
        motivation,
        internet,
        gender,
        age,
        learning_style,
        online_courses,
        discussions,
        assignment_completion,
        edutech,
        stress_level
    ]], columns=feature_columns)

    prediction = model.predict(input_data)

    st.success(f"Predicted Final Grade: {prediction[0]}")