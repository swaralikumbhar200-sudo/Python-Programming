#Train the model with:
#max_depth = None
#Calculate:
#1.Training accuracy
#2.Testing accuracy
#If training accuracy is 100% but testing accuracy is lower, explain why this happens?

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
#Step 3 : Split the Dataset for Training and Testing- model
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

model = DecisionTreeClassifier(max_depth=None)

print("Model gets created Successfully")

######################################################################
#Step 4 : Train and test the model
######################################################################

print(Border)
print("Step 5 : Train the model")
print(Border)

model.fit(X_train,Y_train)

print("Model Trained Successfully")

Y_pred_train= model.predict(X_train)

Training_accuracy = accuracy_score(Y_train,Y_pred_train)
print("Training_Accuracy: ",Training_accuracy*100, "%")

Y_pred = model.predict(X_test)

Testing_accuracy = accuracy_score(Y_test,Y_pred)
print("Testing_Accuracy: ",Testing_accuracy*100, "%")

######################################################################
#Step 5 : Compare training and testing accuracies
######################################################################

print(Border)
print("Step 5 : Compare training and testing accuracies")
print(Border)

difference = Training_accuracy - Testing_accuracy
print("Accuracy Difference:", difference * 100, "%")

if difference > 0:
    print("Training accuracy is higher than testing accuracy.")
    print("The model may be overfitting.")
elif difference == 0:
    print("Both accuracies are same.")
else:
    print("Testing accuracy is higher than training accuracy.")