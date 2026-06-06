# 🎓 Student Performance Prediction System using Machine Learning & Flask

## 📌 Project Description

The **Student Performance Prediction System** is a Machine Learning-based web application designed to predict a student's academic performance using various educational and lifestyle factors.

This project integrates:

* 📊 Data Science
* 🤖 Machine Learning
* 🌐 Flask Web Development
* 🎨 Frontend Design
* 📈 Model Evaluation

The system takes user inputs such as:

* Hours Studied
* Previous Scores
* Extracurricular Activities
* Sleep Hours
* Sample Question Papers Practiced

and predicts the student's **Performance Index** using a trained **Linear Regression Model**.

This project is highly suitable for:

* Machine Learning beginners
* Flask learners
* Final year mini projects
* Portfolio projects
* Educational analytics systems

---

# 🚀 Key Features

## ✅ Machine Learning Integration

* Uses **Linear Regression Algorithm**
* Trains model using real student performance data
* Predicts performance accurately

---

## ✅ Flask Web Application

* Interactive web interface
* Real-time prediction
* Backend model integration
* Lightweight and fast

---

## ✅ Data Processing

* Dataset preprocessing
* Handling categorical values
* Feature engineering

---

## ✅ Model Evaluation

The model performance is evaluated using:

* 📈 R² Score
* 📉 RMSE (Root Mean Squared Error)

---

## ✅ Model Serialization

* Saves trained model using `pickle`
* Reloads model instantly for predictions

---

## ✅ User-Friendly Interface

* Clean UI
* Styled input forms
* Responsive button effects
* Prediction display on webpage

---

# 🧠 Problem Statement

Educational institutions often need a way to analyze and predict student performance based on multiple academic and personal factors.

This project aims to:

* Predict student performance efficiently
* Reduce manual analysis
* Help understand performance patterns
* Demonstrate ML deployment using Flask

---

# 🏗️ System Architecture

```text id="3v7d92"
                 ┌──────────────────┐
                 │   User Inputs    │
                 └────────┬─────────┘
                          │
                          ▼
                 ┌──────────────────┐
                 │ Flask Web App    │
                 └────────┬─────────┘
                          │
                          ▼
                 ┌──────────────────┐
                 │ Trained ML Model │
                 └────────┬─────────┘
                          │
                          ▼
                 ┌──────────────────┐
                 │ Prediction Result│
                 └──────────────────┘
```

---

# 🛠️ Technologies Used

## 💻 Programming Language

* Python

---

## 🌐 Web Framework

* Flask

---

## 🤖 Machine Learning

* Scikit-learn
* Linear Regression

---

## 📊 Data Processing

* Pandas
* NumPy

---

## 📈 Visualization

* Matplotlib

---

## 🎨 Frontend

* HTML5
* CSS3

---

## 📦 Model Serialization

* Pickle

---

# 📂 Project Structure

```bash id="n1h7bz"
Student-Performance-Prediction/
│
├── app.py
├── model.py
├── model.pkl
├── requirements.txt
├── Student_Performance.csv
│
├── templates/
│   └── index.html
│
└── README.md
```

---

# 📄 File Description

## 🔹 app.py

Main Flask application.

Responsibilities:

* Loads trained ML model
* Handles routes
* Accepts user inputs
* Predicts student performance
* Displays prediction on webpage

---

## 🔹 model.py

Machine Learning pipeline.

Includes:

* Dataset loading
* Data preprocessing
* Model training
* Testing
* Prediction
* Model saving

---

## 🔹 model.pkl

Serialized trained Linear Regression model.

Purpose:

* Avoid retraining every time
* Fast prediction loading

---

## 🔹 index.html

Frontend webpage.

Features:

* Input forms
* Dropdown menu
* Styled UI
* Prediction display

---

## 🔹 requirements.txt

Contains all required dependencies for the project.

---

## 🔹 Student_Performance.csv

Dataset used for training and testing the model.

---

# 📊 Dataset Information

The dataset contains several attributes related to student academic performance.

## 📌 Features Used

| Feature                    | Description                      |
| -------------------------- | -------------------------------- |
| Hours Studied              | Number of study hours            |
| Previous Scores            | Student's previous marks         |
| Extracurricular Activities | Participation in activities      |
| Sleep Hours                | Average sleeping hours           |
| Sample Questions Practiced | Number of practice papers solved |

---

## 🎯 Target Variable

| Variable          | Description                 |
| ----------------- | --------------------------- |
| Performance Index | Final predicted performance |

---

# ⚙️ Data Preprocessing

The project performs preprocessing before training.

## Steps Included:

* Loading CSV dataset
* Checking missing values
* Data type verification
* Encoding categorical values

---

## 🔄 Categorical Encoding

```python id="7kwx1k"
'Yes' → 1
'No'  → 0
```

---

# 🤖 Machine Learning Model

## 📌 Algorithm Used

### Linear Regression

Linear Regression is used because:

* It is simple and efficient
* Works well for numerical prediction
* Easy to interpret
* Suitable for regression tasks

---

# 🔍 Model Training Process

## Step 1: Train-Test Split

Dataset split:

* 80% Training Data
* 20% Testing Data

```python id="3t4gcv"
train_test_split(test_size=0.2, random_state=7)
```

---

## Step 2: Model Training

```python id="zjlwmj"
model = LinearRegression()
model.fit(X_train, y_train)
```

---

## Step 3: Prediction

```python id="nrv5y8"
prediction = model.predict(features)
```

---

# 📈 Model Evaluation Metrics

## ✅ R² Score

Measures prediction accuracy.

Formula:

```text id="s6o0up"
R² = 1 - (SSR / SST)
```

Higher value indicates better performance.

---

## ✅ Root Mean Squared Error (RMSE)

Measures prediction error.

Formula:

```text id="23mtv9"
RMSE = √(Σ(actual - predicted)² / n)
```

Lower RMSE indicates better model performance.

---

# 🌐 Flask Application Workflow

## 🧩 Step-by-Step Process

### 1️⃣ User Opens Webpage

The Flask server renders:

```text id="vxccau"
index.html
```

---

### 2️⃣ User Enters Inputs

Inputs include:

* Hours Studied
* Previous Scores
* Sleep Hours
* Activities

---

### 3️⃣ Form Submission

Data is sent to:

```text id="w9q5kr"
/predict
```

---

### 4️⃣ Flask Backend Processes Data

* Converts inputs
* Encodes categorical values
* Creates NumPy array

---

### 5️⃣ Model Prediction

Loaded ML model predicts performance.

---

### 6️⃣ Output Display

Prediction appears on webpage dynamically.

---

# 🖥️ Frontend UI Features

## 🎨 UI Styling Includes:

* Large title text
* Rounded input fields
* Hover effects
* Clean alignment
* Responsive spacing

---

# 📦 Installation Guide

# Step 1️⃣ Clone Repository

```bash id="a6v6ec"
git clone <repository-url>
cd Student-Performance-Prediction
```

---

# Step 2️⃣ Create Virtual Environment

## Windows

```bash id="t56h0z"
python -m venv venv
venv\Scripts\activate
```

## Linux / Mac

```bash id="hqqmhh"
python3 -m venv venv
source venv/bin/activate
```

---

# Step 3️⃣ Install Dependencies

```bash id="e0y9wl"
pip install -r requirements.txt
```

---

# ▶️ Running the Project

# Step 1️⃣ Train Model

```bash id="a8p7zc"
python model.py
```

This will:

* Train model
* Test model
* Save `model.pkl`

---

# Step 2️⃣ Start Flask Server

```bash id="vwf4p4"
python app.py
```

---

# Step 3️⃣ Open Browser

Visit:

```text id="2rv2u0"
http://127.0.0.1:5000/
```

---

# 🧪 Sample Input & Output

## 📥 Input Example

| Feature                    | Value |
| -------------------------- | ----- |
| Hours Studied              | 7     |
| Previous Scores            | 85    |
| Extracurricular Activities | Yes   |
| Sleep Hours                | 6     |
| Sample Questions Practiced | 12    |

---

## 📤 Predicted Output

```text id="x3d4zm"
Performance Index = 89.42
```

---

# 🔐 Error Handling

The project uses:

```python id="8y4rqv"
try-except
```

for:

* Runtime exception handling
* Debugging
* Preventing application crashes

---

# 📚 Required Libraries

Main dependencies include:

```text id="yyp4mv"
Flask
NumPy
Pandas
Matplotlib
Scikit-learn
Gunicorn
Pickle
```

---

# 📋 requirements.txt

Install all dependencies:

```bash id="e52k7n"
pip install -r requirements.txt
```

---

# ☁️ Deployment Options

This project can be deployed on:

* Render
* Railway
* Heroku
* AWS
* PythonAnywhere

---

# 🚀 Future Enhancements

## 📊 Planned Improvements

### ✅ Advanced ML Algorithms

* Random Forest
* XGBoost
* Gradient Boosting

---

### ✅ Better UI

* Bootstrap integration
* Dark mode
* Responsive design

---

### ✅ Authentication System

* Login/Signup
* User dashboard

---

### ✅ Database Integration

* MySQL
* PostgreSQL
* SQLite

---

### ✅ Analytics Dashboard

* Performance graphs
* Data visualization
* Accuracy charts

---

### ✅ API Integration

Create REST APIs for predictions.

---

# 📖 Educational Value

This project helps in learning:

* Machine Learning basics
* Flask deployment
* Data preprocessing
* Model evaluation
* Full-stack ML integration

---

# 🎯 Learning Outcomes

After completing this project, you will understand:

✅ Regression problems
✅ Flask routing
✅ HTML form handling
✅ Model serialization
✅ Frontend-backend integration
✅ Real-world ML deployment

---

# 👨‍💻 Author

Developed using:

* Python
* Flask
* Machine Learning
* Scikit-learn

---

# 📜 License

This project is open-source and available for educational and learning purposes.

---

# ⭐ Conclusion

The **Student Performance Prediction System** is a complete end-to-end Machine Learning web application that demonstrates how predictive analytics can be integrated with Flask to build real-world educational systems.

This project successfully combines:

* Data Science
* Machine Learning
* Model Evaluation
* Flask Development
* Frontend Design

into a single practical application.

It serves as an excellent project for:

* Students
* Beginners
* Data Science enthusiasts
* Flask developers
* Portfolio showcasing

---
