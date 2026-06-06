import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pickle
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score,root_mean_squared_error
import sys
import os
import warnings
warnings.filterwarnings("ignore")


class Student_Performance:
    def __init__(self,path):
        try:
            self.path=path
            self.df=pd.read_csv(self.path)
            print(self.df.head())
            print(self.df.shape)
            print(self.df.isna())
            print(self.df.dtypes)
            self.df['Extracurricular Activities'] = self.df['Extracurricular Activities'].map({'No': 0, 'Yes': 1})
            self.X=self.df.drop(['Performance Index'],axis=1)
            self.y=self.df['Performance Index']
            self.X_train,self.X_test,self.y_train,self.y_test=train_test_split(self.X,self.y,test_size=0.2,random_state=7)
        except Exception as e:
            er_type, er_msg, er_line = sys.exc_info()
            print(f"{er_type} Error Occured in {er_line.tb_lineno} number because {er_msg}")
    def training(self):
        try:
            self.model=LinearRegression()
            self.model.fit(self.X_train,self.y_train)
            print("Training Completed")
            print(f"Training Accuracy:{r2_score(self.y_train,self.model.predict(self.X_train))*100}")
            print(f"Training Loss:{root_mean_squared_error(self.y_train,self.model.predict(self.X_train))}")
        except Exception as e:
            er_type, er_msg, er_line = sys.exc_info()
            print(f"{er_type} Error Occured in {er_line.tb_lineno} number because {er_msg}")
    def testing(self):
        try:
            print("Testing Completed")
            print(f"Testing Accuracy:{r2_score(self.y_test,self.model.predict(self.X_test))*100}")
            print(f"Testing Loss:{r2_score(self.y_test,self.model.predict(self.X_test))}")
        except Exception as e:
            er_type, er_msg, er_line = sys.exc_info()
            print(f"{er_type} Error Occured in {er_line.tb_lineno} number because {er_msg}")
    def sample_input(self,hours_studied,previous_scores,extra_curricular_activities,sleeping_hours,sample_practiced):
        try:
            m=self.model.predict([[hours_studied,previous_scores,extra_curricular_activities,sleeping_hours,sample_practiced]])
            print(m)
        except Exception as e:
            er_type, er_msg, er_line = sys.exc_info()
            print(f"{er_type} Error Occured in {er_line.tb_lineno} number because {er_msg}")
    def plotting(self):
        plt.figure(figsize=(5,3))
        plt.scatter(x=self.X_train,y=self.y_train,color="red",marker="*")
        plt.plot(self.X_train,self.model.predict(self.X_train),color="blue")
        plt.show()
    def save_model(self):
        try:
            with open('model.pkl','wb') as f:
                pickle.dump(self.model,f)
        except Exception as e:
            er_type, er_msg, er_line = sys.exc_info()
            print(f"{er_type} Error Occured in {er_line.tb_lineno} number because {er_msg}")
if __name__=="__main__":
    try:
        path = r"C:\Users\mpriy\Downloads\Student_Performance\data\Student_Performance.csv"
        hours_studied = int(input("Enter Hours:"))
        previous_scores = int(input("Enter Previous Scores:"))
        extra_curricular_activities = input("Enter whether student plays Extracurricular Activities (Yes/No):")
        if extra_curricular_activities == "Yes":
            extra_curricular_activities = 1
        else:
            extra_curricular_activities = 2
        sleeping_hours = int(input("Enter Sleeping Hours:"))
        sample_practiced = int(input("Enter Sample Question Papers Practiced:"))
        obj = Student_Performance(path)
        obj.training()
        obj.testing()
        obj.sample_input(hours_studied, previous_scores, extra_curricular_activities, sleeping_hours, sample_practiced)
        obj.save_model()
        with open('model.pkl', 'rb') as f:
            m = pickle.load(f)
            print(m.predict(
                [[hours_studied, previous_scores, extra_curricular_activities, sleeping_hours, sample_practiced]]))
    except Exception as e:
        er_type, er_msg, er_line = sys.exc_info()
        print(f"{er_type} Error Occured in {er_line.tb_lineno} number because {er_msg}")