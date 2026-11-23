#Implement Simple Linear Regression manually without using any ML library.
#Dataset:
#X = [1, 2, 3, 4, 5]
#Y = [3, 4, 2, 4, 5]

#Tasks
#Calculate:
#1.Mean of X (X̄)
#2.Mean of Y (Ȳ)
#3.Slope (m)
#4.Intercept (c)


import numpy as np


Border = "-" * 40
######################################################################
#Step 1 : Load the dataset
######################################################################

print(Border)
print("Step 1 : Load the dataset")
print(Border)

X = [1, 2, 3, 4, 5]
Y = [3, 4, 2, 4, 5]

print("Independent Values are: ",X)
print("Dependent Values are: ",Y)

print(Border)

######################################################################
#Step 2 : Mean of X and Y 
######################################################################

print(Border)
print("Step 2 : Mean of X and Y ")
print(Border)

sum_x = 0
sum_y = 0

for i in range(len(X)):
    sum_x = sum_x + X[i]
    sum_y = sum_y + Y[i]

Mean_X = sum_x/len(X)
Mean_Y = sum_y/len(Y)

print("Mean of X: ", Mean_X)
print("Mean of Y: ", Mean_Y)

print(Border)

######################################################################
#Step 3 : Slope (m)
######################################################################

print(Border)
print("Step 3 : Slope (m)")
print(Border)

#m = summation(x-xbar)(y-ybar)/summation(x-xbar)**2
Numerator = 0
Denomenator = 0
n =len(X)

for i in range(n):
    Numerator = Numerator +((X[i]-Mean_X)*(Y[i]-Mean_Y))
    Denomenator = Denomenator + ((X[i]-Mean_X)**2)

m = Numerator/Denomenator

print("Slope (m): ", m)

print(Border)

######################################################################
#Step 4 : Intercept (C)
######################################################################

print(Border)
print("Step 4 : Intercept (C)")
print(Border)

#y =mx+c
#c = ymean - m * xmean

C = Mean_Y - m * Mean_X
print("Intercept (c): ",C)

print(Border)

######################################################################
#Step 5 : Regression Equation
######################################################################

print(Border)
print("Step 5 : Regression Equation")
print(Border)

print("Regression Equation is: Y=",m,"X +",C)

X_new = 6

Predicted_Y = m * X_new + C

print("Predicted Y for X = 6:", Predicted_Y)

print(Border)


