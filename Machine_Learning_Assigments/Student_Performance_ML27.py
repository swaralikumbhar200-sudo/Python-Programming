#Create a new column:
#PerformanceIndex = (StudyHours * 2) + Attendance
#Train the model including this new feature.
#Does the accuracy improve?

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

Border = "-"* 30

######################################################################
#Step 1 : Load the dataset
######################################################################

print(Border)
print("Step 1 : Load the dataset")
print(Border)

Datapath = "student_performance_ml.csv"

df = pd.read_csv(Datapath)

#X : Independent Variable / Features
#Y : Dependent Variable / Labels

feature_cols =[
    "StudyHours",
    "Attendance",
    "PreviousScore",
    "AssignmentsCompleted",
    "SleepHours"
]

X1 = df[feature_cols]
Y1 = df["FinalResult"]

print("X Shape: ",X1.shape)
print("Y Shape: ",Y1.shape)
######################################################################
#Step 2 : Split the Dataset for Training and Testing- model
######################################################################

print(Border)
print("Step 3 : Split the Dataset for Training and Testing")
print(Border)

X_train1, X_test1, Y_train1, Y_test1= train_test_split(X1,Y1,test_size=0.5,random_state=42)

print("Dataset splitting Activity done")

model = DecisionTreeClassifier()

print("Model gets created Successfully")

model.fit(X_train1,Y_train1)

print("Model Trained Successfully")

Y_pred = model.predict(X_test1)

Testing_accuracy = accuracy_score(Y_test1,Y_pred)
print("Testing_Accuracy: ",Testing_accuracy*100, "%")

######################################################################
#Step 3 : Added new feature in existing dataset
######################################################################

print(Border)
print("Step 3 : Added new feature in existing dataset")
print(Border)

df["PerformanceIndex"] =(df["StudyHours"]*2)+df["Attendance"]
print(df)

#X : Independent Variable / Features
#Y : Dependent Variable / Labels

feature_cols =[
    "StudyHours",
    "Attendance",
    "PreviousScore",
    "AssignmentsCompleted",
    "SleepHours",
    "PerformanceIndex"
]

X2 = df[feature_cols]
Y2 = df["FinalResult"]

print("X Shape: ",X2.shape)
print("Y Shape: ",Y2.shape)

######################################################################
#Step 4 : Split the Dataset for Training and Testing of new_model
######################################################################

print(Border)
print("Step 4 : Split the Dataset for Training and Testing of new_model")
print(Border)

X_train2,X_test2,Y_train2 ,Y_test2 = train_test_split(X2,Y2,test_size=0.5,random_state=42)

print("Dataset splitting Activity done")

print("X: ",X2.shape)
print("Y: ",Y2.shape)

model_new = DecisionTreeClassifier()

print("Model gets created Successfully")

model_new.fit(X_train2,Y_train2)

print("Model Trained Successfully")

Y_pred_new = model_new.predict(X_test2)

Testing_accuracy_new = accuracy_score(Y_test2,Y_pred_new)
print("Testing_Accuracy_new: ",Testing_accuracy_new*100, "%")

######################################################################
#Step 5 : Compare both Accuracies
######################################################################

print(Border)
print("Step 5 : Compare both Accuracies")
print(Border)

print("Testing_Accuracy: ",Testing_accuracy*100, "%")
print("Testing_Accuracy_new: ",Testing_accuracy_new*100, "%")

if Testing_accuracy_new > Testing_accuracy:
    print("Accuracy improved after adding PerformanceIndex.")

elif Testing_accuracy_new < Testing_accuracy:
    print("Accuracy decreased after adding PerformanceIndex.")

else:
    print("Accuracy remained the same after adding PerformanceIndex.")
