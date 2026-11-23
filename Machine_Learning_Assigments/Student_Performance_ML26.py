#Decision Tree Visualization
#Use:
#from sklearn.tree import plot_tree
#Visualize the trained decision tree.
#1.Which feature appears at the root node?
#2.Why do you think that feature was selected first?


import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import plot_tree
from sklearn.tree import DecisionTreeClassifier
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
print("Step 7 : Train the model")
print(Border)

model.fit(X_train,Y_train)

print("Model Trained Successfully")

######################################################################
#Step 6 : Plot tree
######################################################################

print(Border)
print("Step 6 : Plot tree")
print(Border)

plt.figure(figsize=(15,11))

plot_tree(model,filled=True,feature_names= feature_cols,class_names= True)

plt.title("Student Performance Decision Tree")

plt.show()

#1. PreviousScore is the feature appears at the root node
#2. It was selected first because it provides the best split for predicting FinalResult and gives the highest reduction in impurity.