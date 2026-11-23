#Write a single structured Python program that performs:
#1.Dataset loading
#2.Data analysis
#3.Visualization
#4.Train-test split
#5.Model training
#6.Prediction
#7.Accuracy calculation
#8.Confusion matrix generation
#9.Final conclusion
#Your code should include proper comments explaining each step.

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import (
    accuracy_score,
    confusion_matrix)

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
#Step 2 : Data Analysis(EDA)
######################################################################

print(Border)
print("Step 2 : Data Analysis(EDA)")
print(Border)

print("Shape of Dataset: ",df.shape)

print("Column names: ",list(df.columns))

print("Missing values per column: ")
print(df.isnull().sum())

print("Class Distribution (Final Result Count)")
print(df["FinalResult"].value_counts())

print("Stastical report of dataset: ")
print(df.describe())

######################################################################
#Step 3 : Visualization Of Dataset
######################################################################

print(Border)
print("Step 3 : Visualization Of Dataset")
print(Border)

#Scatter plot
plt.figure(figsize=(7,5))

for sp in df["FinalResult"].unique():
    temp = df[df["FinalResult"] == sp]
    plt.scatter(temp["StudyHours"],temp["PreviousScore"],label = sp)

plt.title("Student Performance Case Study")

plt.xlabel("StudyHours")
plt.ylabel("Previous Score")


plt.legend()
plt.grid()
plt.show()

######################################################################
#Step 4 : Split the Dataset for Training and Testing
######################################################################

print(Border)
print("Step 4 : Split the Dataset for Training and Testing")
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

X_train, X_test, Y_train, Y_test = train_test_split(X,Y, test_size = 0.5, random_state =42)

print("Dataset splitting Activity done")

print("X: ",X.shape)       #(150,4)
print("Y: ",Y.shape)       #(150,)

print("X_train: ",X_train.shape)  #(75,4)
print("X_test: ",X_test.shape)   #(75,4)

print("Y_train: ",Y_train.shape)  #(75,)
print("Y_test: ",Y_test.shape)  #(75,)

######################################################################
#Step 5 : Train the model
######################################################################

print(Border)
print("Step 5 : Train the model")
print(Border)

model = DecisionTreeClassifier()

print("Model Created Successfully")

model.fit(X_train,Y_train)

print("Model Trained Sucessfully")

######################################################################
#Step 6 : Test the model and Prediction
######################################################################

print(Border)
print("Step 6 : Test the model and Prediction")
print(Border)

Y_pred = model.predict(X_test)

print("Predicted Answers are: ",Y_pred)

######################################################################
#Step 7 : Accuracy Calculation
######################################################################

print(Border)
print("Step 7 : Accuracy Calculation")
print(Border)

Accuracy_Model = accuracy_score(Y_test,Y_pred)
print("Accuracy of model is: ",Accuracy_Model*100 , "%")

######################################################################
#Step 8 : Confusion Matrix Generation
######################################################################

print(Border)
print("Step 8 : Confusion Matrix Generation")
print(Border)

ConfusionMatrix= confusion_matrix(Y_test,Y_pred)
print("Confusion Matrix is: \n",ConfusionMatrix)

######################################################################
#Step 9 : Final Conclusion
######################################################################

print(Border)
print("Step 9 : Final Conclusion")
print(Border)

print("The Decision Tree model was trained successfully.")
print("The model accuracy is:", Accuracy_Model * 100, "%")

if Accuracy_Model >= 0.90:
    print("Conclusion: The model has good performance.")
elif Accuracy_Model >= 0.70:
    print("Conclusion: The model has acceptable performance.")
else:
    print("Conclusion: The model performance can be improved.")