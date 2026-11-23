#Write a Python program that calculates the variance and standard deviation of the dataset:
#[6,7,8,9,10,11,12]
# Display both results.

import numpy as np

Border = "-" * 40
######################################################################
#Step 1 : Load the dataset
######################################################################

print(Border)
print("Step 1 : Load the dataset")
print(Border)

X =[6,7,8,9,10,11,12]

print("Values in the Dataset: ",X)
print(Border)

######################################################################
#Step 2 : Mean Of Dataset
######################################################################

print(Border)
print("Step 2 : Mean Of dataset")
print(Border)

sum_x = 0

for i in range(len(X)):
    sum_x = sum_x + X[i]

Mean_X = sum_x / len(X)

print("Mean of the Dataset is: ",Mean_X)
print(Border)

######################################################################
#Step 3 : Variance Of Dataset
######################################################################

print(Border)
print("Step 2 : Mean Of dataset")
print(Border)

numerator = 0
denomenator = 0

for i in range(len(X)):
    numerator = numerator +((X[i]-Mean_X))**2
    denomenator = len(X)

variance = numerator / denomenator

print("Variance of the Dataset is: ",variance)
print(Border)    

######################################################################
#Step 3 : Standard Deviation Of Dataset
######################################################################

print(Border)
print("Step 3 : Standard Deviation Of dataset")
print(Border)

standard_deviation = np.sqrt(variance)
print("Standard Deviation of the Dataset is: ",standard_deviation) 

print(Border)