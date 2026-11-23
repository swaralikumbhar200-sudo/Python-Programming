#Consider the dataset below:
#StudyHours	SleepHours	Marks
#    1	       7	      50
#    2	       6	      55
#    3	       7	      60
#    4	       6	      65
#    5	       8	      70
#Write a Python program to:
#1. Train a regression model using this dataset.
#2. Print the coefficients for both features.
#3. Print the intercept.

import pandas as pd

from sklearn.linear_model import LinearRegression

Border = "-" * 40

######################################################################
#Step 1 : Load the dataset
######################################################################

print(Border)
print("Step 1 : Load the dataset")
print(Border)

df = pd.DataFrame({
    "StudyHours" : [1,2,3,4,5],
    "SleepHours" : [7,6,7,6,8],
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

X = df[["StudyHours","SleepHours"]]
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

model =LinearRegression()

model.fit(X,Y)
print("Model Trained Successfully..")
print(Border)

######################################################################
#Step 4 : Display Model Parameters
######################################################################

print(Border)
print("Step 4 : Display Model Parameters")
print(Border)

print("Coefficient of StudyHours: ",model.coef_[0])
print("Coefficient of SleepHours: ",model.coef_[1])

print("Y - intercept is: ",model.intercept_)
print(Border)