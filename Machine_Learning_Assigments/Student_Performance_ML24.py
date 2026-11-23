#Identify students where:
#y_test != y_pred
#1.Display those rows.
#2.How many students were misclassified?
#3.What common pattern do you observe?

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

######################################################################
#Step 2 :Decide the dependent and Independent Variables
######################################################################

print(Border)
print("Step 2 :Decide the dependent and Independent Variables")
print(Border)

#X : Independent Variable / Features
#Y : Dependent Variable / Labels

feature_cols =[
    "StudyHours",
    "Attendance",
    "PreviousScore",
    "AssignmentsCompleted",
    "SleepHours"
]

X = df[feature_cols]
Y = df["FinalResult"]

print("X Shape: ",X.shape)
print("Y Shape: ",Y.shape)
######################################################################
#Step 3 : Split the Dataset for Training and Testing
######################################################################

print(Border)
print("Step 3 : Split the Dataset for Training and Testing")
print(Border)

X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size=0.5,random_state=42)

print("Dataset splitting Activity done")

print("X_train: ",X_train.shape)
print("X_test: ",X_test.shape)

print("Y_train: ",Y_train.shape)
print("Y_test: ",Y_test.shape)

######################################################################
#Step 4 : Build the model
######################################################################

print(Border)
print("Step 4 : Build the model")
print(Border)

model = DecisionTreeClassifier()

print("Model gets created Successfully")

######################################################################
#Step 5 : Train and Test the model
######################################################################

print(Border)
print("Step 5 : Train and Test the model")
print(Border)

model.fit(X_train,Y_train)

print("Model Trained Successfully")

Y_pred = model.predict(X_test)
print("Predicted answers are: ",Y_pred.tolist())

print("Expected Answers are: ",Y_test.tolist())

######################################################################
#Step 6 : Find Misclassified Students
######################################################################

print(Border)
print("Step 6 : Find Misclassified Students")
print(Border)

misclassified = Y_test != Y_pred

print("Missclassified Students: ")
print(X_test[misclassified])

print("Number of misclassified students: ",misclassified.sum())

#No clear common pattern can be observed because only one student was misclassified.