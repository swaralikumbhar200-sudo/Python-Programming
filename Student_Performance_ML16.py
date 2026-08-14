#Train three Decision Tree models with:
#1.max_depth = 1
#2.max_depth = 3
#3.max_depth = None
#Compare their testing accuracies and write your observations.


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

print("X: ",X.shape)
print("Y: ",Y.shape)

print("X_train: ",X_train.shape)
print("X_test: ",X_test.shape)


print("Y_train: ",Y_train.shape)
print("Y_test: ",Y_test.shape)

######################################################################
#Step 4 :  first model
######################################################################

print(Border)
print("Step 4 : First model")
print(Border)

model1 = DecisionTreeClassifier(max_depth=1)

print("First Model created Successfully")

model1.fit(X_train,Y_train)

print("First Model Trained Successfully")

Y_pred1 = model1.predict(X_test)
Testing_Accuracy1 = accuracy_score(Y_test,Y_pred1)

print("Predicted answers are: ",Y_pred1)

print("Testing Accuracy : ",Testing_Accuracy1*100,"%")

######################################################################
#Step 5 :  Second model
######################################################################

print(Border)
print("Step 5 : Second model")
print(Border)

model2 = DecisionTreeClassifier(max_depth=3)

print("Second Model created Successfully")

model2.fit(X_train,Y_train)

print("Second Model Trained Successfully")

Y_pred2 = model2.predict(X_test)

print("Predicted answers are: ",Y_pred2)
Testing_Accuracy2 = accuracy_score(Y_test,Y_pred2)

print("Testing Accuracy : ",Testing_Accuracy2*100,"%")

######################################################################
#Step 6 :  Third model
######################################################################

print(Border)
print("Step 6 : Third model")
print(Border)

model3 = DecisionTreeClassifier(max_depth=None)

print("Third Model created Successfully")

model3.fit(X_train,Y_train)

print("Third Model Trained Successfully")

Y_pred3 = model3.predict(X_test)

print("Predicted answers are: ",Y_pred3)
Testing_Accuracy3 = accuracy_score(Y_test,Y_pred3)

print("Testing Accuracy : ",Testing_Accuracy3*100,"%")

#All three Decision Tree models achieved the same testing accuracy of 93.33%. Therefore, changing the max_depth from 1 to 3 or None did not affect the testing accuracy on this dataset.