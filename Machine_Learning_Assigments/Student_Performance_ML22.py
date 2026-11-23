#Create a new DataFrame with details of 5 new students.
#1.Use the trained model to predict their results.
#2.Display the predictions clearly.

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

Border = "-"* 30

######################################################################
#Step 1 : Load the dataset
######################################################################

print(Border)
print("Step 1 : Load the dataset")
print(Border)

Datapath = "student_performance_ml.csv"
df = pd.read_csv(Datapath)
print("Data loaded Successfully")

######################################################################
#Step 2 : Split the Dataset for Training and Testing for model
######################################################################

print(Border)
print("Step 2 : Split the Dataset for Training and Testing")
print(Border)

feature_cols =[
    "StudyHours",
    "Attendance",
    "PreviousScore",
    "AssignmentsCompleted",
    "SleepHours"
]

X = df[feature_cols]
Y = df["FinalResult"]

X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.5,random_state=42)

model = DecisionTreeClassifier()

model.fit(X_train,Y_train)

print("Model Created and Trained Successfully")

######################################################################
#Step 3 : Create the Dataframe
######################################################################

print(Border)
print("Step 3 :Create the Dataframe")
print(Border)

Data ={
        "StudyHours": [2.0, 3.0, 4.0, 5.0, 6.0,],
        "Attendance" : [65,70,75,80,85],
        "PreviousScore" : [45,50,55,60,65],
        "AssignmentsCompleted" : [3,4,5,6,7],
        "SleepHours" :[5,6,6,7,7],
        
    }

dobj = pd.DataFrame(Data)
print(dobj)

######################################################################
#Step 4 : Predict the results
######################################################################

print(Border)
print("Step 4 : Predict the results")
print(Border)

X_new = dobj[feature_cols]

Y_pred = model.predict(X_new)

print("Predicted Answers are : ",Y_pred)