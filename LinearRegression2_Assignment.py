#Write a Python program using LinearRegression to train a regression model using the given dataset.
#Study Hours	   Marks
#  1	             50
#  2	             55
#  3	             60
#  4	             65
#  5	             70
#Your program should:
#1. Train the regression model
#2. Print the coefficient
#3. Print the intercept

#Using the regression model created , write a Python program to predict marks 
# for 6 study hours and display the predicted value.


import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

Border = "-" * 40

######################################################################
#Step 1 : Load the dataset
######################################################################

print(Border)
print("Step 1 : Load the dataset")
print(Border)

df = pd.DataFrame({
    "Study Hours":[1,2,3,4,5],
    "Marks" : [50,55,60,65,70]
})

print(df)

print(Border)

######################################################################
#Step 2 : Separate Independent and Dependent Variables
######################################################################

print(Border)
print("Step 2 : Separate Independent and Dependent Variables")
print(Border)

X = df[["Study Hours"]]
Y = df["Marks"]

print("X shape: ",X.shape)
print("Y shape: ",Y.shape)

print(Border)

######################################################################
#Step 3 : Train the Regression Model
######################################################################

print(Border)
print("Step 3 : Train the Regression Model")
print(Border)

model = LinearRegression()

model.fit(X,Y)

print("Model Trained Successfully..")
print(Border)

######################################################################
#Step 4 : Display Model Parameters
######################################################################

print(Border)
print("Step 4 : Display Model Parameters")
print(Border)

print("Coefficient: ",model.coef_)
print("Y - intercept is: ",model.intercept_)

print(Border)

######################################################################
#Step 5 : Prediction 
######################################################################

print(Border)
print("Step 5 : Prediction")
print(Border)

new_StudyHours = pd.DataFrame({
    "Study Hours" : [6]
    })

Prediction = model.predict(new_StudyHours)

print("Predicted Marks for 6 study hours: ",Prediction)