#Write a Python program that calculates the mean of a dataset using NumPy for the following values:
#[6,7,8,9,10,11,12]

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

Mean_X = np.mean(X)
print("Mean of the Dataset is: ",Mean_X)

print(Border)