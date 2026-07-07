# Student Performance Prediction using Machine Learning

## Project Overview

Student Performance Prediction is a Machine Learning project that predicts a student's **Final Grade** based on academic performance, learning behavior, and personal factors.

The project uses the **Random Forest Classifier** algorithm and provides an interactive web application built with **Streamlit** for real-time grade prediction.



## Features

- Data Preprocessing
- Exploratory Data Analysis (EDA)
- Multi-Class Classification
- Feature Selection
- Random Forest Machine Learning Model
- Model Evaluation
- Streamlit Web Application
- Real-Time Student Grade Prediction



##  Dataset

The dataset contains **14,003 student records** with the following features:

| Feature |
|----------|
| StudyHours |
| Attendance |
| Resources |
| Extracurricular |
| Motivation |
| Internet |
| Gender |
| Age |
| LearningStyle |
| OnlineCourses |
| Discussions |
| AssignmentCompletion |
| EduTech |
| StressLevel |
| FinalGrade (Target Variable) |

> **Note:** The `ExamScore` feature was intentionally removed during model training to prevent **data leakage**, ensuring realistic and reliable predictions.

---

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Streamlit
- Pickle

---

## Machine Learning Model

**Algorithm Used**

- Random Forest Classifier

### Model Performance

| Metric | Value |
|--------|--------|
| Accuracy | **91.97%** |
| Problem Type | Multi-Class Classification |



## Project Structure

```
Student_Performance_Prediction/
│
├── app.py
├── student_performance_model.pkl
├── feature_columns.pkl
├── student_performance.csv
├── requirements.txt
├── README.md
└── screenshots/
```


## Installation

### Clone the repository

```bash
git clone https://github.com/yourusername/Student-Performance-Prediction-ML.git
```

### Go to the project folder

```bash
cd Student-Performance-Prediction-ML
```

### Install dependencies

```bash
pip install -r requirements.txt
```


## Run the Application

```bash
streamlit run app.py
```

The application will open in your browser at:

```
http://localhost:8501
```


## Workflow

1. Load Dataset
2. Data Cleaning
3. Exploratory Data Analysis
4. Feature Selection
5. Train-Test Split
6. Train Random Forest Model
7. Evaluate Model
8. Save Model using Pickle
9. Build Streamlit Application
10. Predict Student Final Grade



## Model Evaluation

The model was evaluated using:

- Accuracy Score
- Confusion Matrix
- Precision
- Recall
- F1-Score

### Final Accuracy

**91.97%**


## Future Enhancements

- Deploy the application on Streamlit Community Cloud
- Compare multiple Machine Learning algorithms
- Hyperparameter tuning
- Add data visualization dashboard
- Improve UI with custom themes
- Connect with a database for storing predictions


## Author

**Pranav Chougule**

Master of Computer Applications (MCA)

Interested in:
- Machine Learning
- Data Science
- Artificial Intelligence
- Python Development

