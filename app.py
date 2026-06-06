import flask
from flask import Flask,render_template,request
import numpy as np
import pickle
import sklearn
from sklearn.linear_model import LinearRegression

with open("model.pkl","rb") as f:
    m = pickle.load(f)

app = Flask(__name__)


@app.route('/')
def initial_fun():
    return render_template("index.html")

@app.route("/predict",methods = ['GET','POST'])
def fun3():
    hours_studied = int(request.form['Hours Studied'])
    previous_scores = int(request.form['Previous Scores'])
    extracuriccular_activities = request.form['Extracurricular Activities']
    sleep_hours = int(request.form['Sleep Hours'])
    sample_question_papers = int(request.form['Sample Questions Practiced'])

    if extracuriccular_activities.lower()=="yes":
        extracuriccular_activities = 1
    else:
        extracuriccular_activities = 0

    # Create input array
    features = np.array([[hours_studied,previous_scores,extracuriccular_activities,sleep_hours,sample_question_papers]])

    # Prediction
    prediction = m.predict(features)
    output = round(prediction[0], 2)
    return render_template("index.html" , prediction_text = output)


if __name__ == "__main__":
    app.run(debug=True)