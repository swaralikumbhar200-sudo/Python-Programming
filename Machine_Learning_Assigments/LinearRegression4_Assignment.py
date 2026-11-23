#Consider the following task:
#1. Train a Linear Regression model.
#2. Predict the salary for 6 years of experience.
#3. Plot the regression line using Matplotlib.
#Dataset
#Experience	 Salary
# 1	         20,000
# 2	         25,000
# 3	         30,000
# 4	         35,000
# 5	         40,000
#Expected Output : Predicted salary for 6 years of experience: ₹45,000
#Graph should display:
#Data points
#Regression line

import numpy as np
import pandas as pd

from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

Border = "-" * 50

######################################################################
#Step 1 : Load the dataset
######################################################################

print(Border)
print("Step 1 : Load the dataset")
print(Border)

df = pd.DataFrame({
    "Experience" : [1,2,3,4,5],
    "Salary" : [20000,25000,30000,35000,40000]
})

print("Dataset is: ")
print(df)
print(Border)

######################################################################
#Step 2 : Separate Independent and Dependent Variables
######################################################################

print(Border)
print("Step 2 : Separate Independent and Dependent Variables")
print(Border)

X = df[["Experience"]]
Y = df["Salary"]

print("X shape: ",X.shape)
print("Y shape: ",Y.shape)

print(Border)

######################################################################
#Step 3 : Train Model
######################################################################

print(Border)
print("Step 3 : Train Model")
print(Border)

model = LinearRegression()

model.fit(X,Y)

print("Model Trained Successfully")

print(Border)

######################################################################
#Step 4 : Prediction
######################################################################

print(Border)
print("Step 4 : Prediction")
print(Border)

new_Experience =pd.DataFrame({"Experience" :[6]})

Y_pred = model.predict(new_Experience)
print("Predicted salary for 6 years of experience: ",Y_pred[0])

print(Border)

######################################################################
#Step 5 : Visualization
######################################################################
print(Border)
print("Step 5 : Visualization")
print(Border)

x = np.linspace(1,5,100).reshape(-1,1)
y = model.predict(x)

plt.plot(x,y,color="g",label="Regression Line")
plt.scatter(X,Y,color="r",label="Data Points")

plt.xlabel("X : Independent Variable")
plt.ylabel("Y: Dependent Variable")

plt.legend()
plt.show()

print(Border)