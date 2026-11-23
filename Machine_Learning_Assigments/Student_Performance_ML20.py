#Remove the column SleepHours from the dataset.
#1.Train the model again.
#2.Compare the new accuracy with the previous accuracy.
#3.Does removing this feature affect the model's performance?

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
print("Data loaded Successfully")

######################################################################
#Step 2 : Split the Dataset for Training and Testing for model1
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

X1 = df[feature_cols]
Y1 = df["FinalResult"]

print("X shape1: ",X1.shape)
print("Y shape1: ",Y1.shape)

X_train1,X_test1,Y_train1,Y_test1 = train_test_split(X1,Y1,test_size=0.5,random_state=42)

print("X_train1: ",X_train1.shape)
print("Y_train1: ",Y_train1.shape)

print("X_test1: ",X_test1.shape)
print("Y_test1: ",Y_test1.shape)

######################################################################
#Step 3 : Train and Test the model1
######################################################################

print(Border)
print("Step 3 : Train and Test the model")
print(Border)

model1 = DecisionTreeClassifier()

model1.fit(X_train1,Y_train1)

print("Model1 trained successfully")

Y_pred1 = model1.predict(X_test1)
print("Predicted Answers are: ",Y_pred1)

Accuracy1 = accuracy_score(Y_test1,Y_pred1)
print("Previous_Accuracy is: ",Accuracy1*100,"%")

######################################################################
#Step 4 : Removing the SleepHours column and splitting for model2
######################################################################

print(Border)
print("Step 4 : Removing the SleepHours column and splitting for model 2")
print(Border)

#deleting SleepHours column:
df = df.drop(columns=["SleepHours"])

feature_cols2 =[
    "StudyHours",
    "Attendance",
    "PreviousScore",
    "AssignmentsCompleted",
]

X2 = df[feature_cols2]
Y2 = df["FinalResult"]

print("X shape2: ",X2.shape)
print("Y shape2: ",Y2.shape)

X_train2,X_test2,Y_train2,Y_test2 = train_test_split(X2,Y2,test_size=0.5,random_state=42)

print("X_train2: ",X_train2.shape)
print("Y_train2: ",Y_train2.shape)

print("X_test2: ",X_test2.shape)
print("Y_test2: ",Y_test2.shape)

######################################################################
#Step 5 : Train and Test the model2
######################################################################

print(Border)
print("Step 5 : Train and Test the model2")
print(Border)

model2 = DecisionTreeClassifier()

model2.fit(X_train2,Y_train2)

print("Model2 trained successfully")

Y_pred2 = model2.predict(X_test2)
print("Predicted Answers are: ",Y_pred2)

Accuracy2 = accuracy_score(Y_test2,Y_pred2)
print("New_Accuracy is: ",Accuracy2*100,"%")

######################################################################
#Step 6 : Comparison between model1 and model2
######################################################################

print(Border)
print("Step 6 : Comparison between model1 and model2")
print(Border)

if Accuracy1 == Accuracy2:
    print("Both models have the same testing accuracy.")
    print("Removing SleepHours did not affect model performance.")
elif Accuracy2 > Accuracy1:
    print("Testing accuracy increased after removing SleepHours.")
    print("Removing SleepHours improved model performance.")
else:
    print("Testing accuracy decreased after removing SleepHours.")
    print("Removing SleepHours reduced model performance.")