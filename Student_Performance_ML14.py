#Generate a confusion matrix using sklearn.
#Display it using ConfusionMatrixDisplay.
#Explain clearly:
#1.True Positive (TP)
#2.True Negative (TN)
#3.False Positive (FP)
#4.False Negative (FN)

import pandas as pd

from sklearn.model_selection import train_test_split

from sklearn.tree import DecisionTreeClassifier

from sklearn.metrics import(
    accuracy_score,
    confusion_matrix,
    classification_report,
    ConfusionMatrixDisplay
)

import matplotlib.pyplot as plt

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

X_train,X_test,Y_train ,Y_test = train_test_split(X,Y,test_size=0.5,random_state=42)

print("Dataset splitting Activity done")

print("X: ",X.shape)
print("Y: ",Y.shape)

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
#Step 5 : Train the model
######################################################################

print(Border)
print("Step 5 : Train the model")
print(Border)

model.fit(X_train,Y_train)

print("Model Trained Successfully")

######################################################################
#Step 6 : Test the model
######################################################################

print(Border)
print("Step 6 : Test the model")
print(Border)

Y_pred = model.predict(X_test)

print("Expected Answers are: ",Y_test)

print("Predicted Answers are: ",Y_pred)

######################################################################
#Step 7 : Accuracy_Score of the Model
######################################################################

print(Border)
print("Step 7 : Accuracy_Score of the Model")
print(Border)

Accuracy = accuracy_score(Y_test,Y_pred)

print("Model Accuracy : ",Accuracy*100)

######################################################################
#Step 8 : Confusion Matrix of the Model
######################################################################

print(Border)
print("Step 8 : Confusion Matrix of the Model")
print(Border)

ConfusionMatrix = confusion_matrix(Y_test,Y_pred)

print("Confusion Matrix is: \n",ConfusionMatrix)

ConfusionMatrixDisplay(confusion_matrix=ConfusionMatrix).plot()

plt.show()

#Assume: Pass = Positive and Fail = Negative
#1.True Negative (TN) = 7 → Actual Fail, predicted Fail
#2.False Positive (FP) = 0 → Actual Fail, predicted Pass
#3.False Negative (FN) = 1 → Actual Pass, predicted Fail
#4.True Positive (TP) = 7 → Actual Pass, predicted Pass
