#After training the Decision Tree model, use: model.feature_importances_
#1.Display the importance score of each feature.
#2.Which feature contributes the most in predicting FinalResult?
#3.Which feature contributes the least?

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
#Step 2 : Split the Dataset for Training and Testing
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

print("X shape: ",X.shape)
print("Y shape: ",Y.shape)

X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.2,random_state=42)

print("X_train: ",X_train.shape)
print("Y_train: ",Y_train.shape)

print("X_test: ",X_test.shape)
print("Y_test: ",Y_test.shape)

######################################################################
#Step 3 : Train the model
######################################################################

print(Border)
print("Step 3 : Train the model")
print(Border)

model = DecisionTreeClassifier()

model.fit(X_train,Y_train)

print("Model trained successfully")


for feature,importance in zip(feature_cols,model.feature_importances_):
    print(feature ,":",importance)

importances = model.feature_importances_

most_important = feature_cols[importances.argmax()]
print("Most Important feature: ",most_important)

least_important = feature_cols[importances.argmin()]
print("Least Important feature: ",least_important)