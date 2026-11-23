# Write a python program to show flattening
# Tasks: 1. Take a 2D matrix, Convert it into 1D vector. 2. Pass it to FC layer and calculate final output manually and explain its role of flatten layer in CNN.

import numpy as np
Border = "-" * 30
# ------------------------------------------------------------  
# Step 1 :  Input Matrix
# ------------------------------------------------------------  
print(Border)
print("Step 1 :  Input Matrix")
print(Border)

Matrix = np.array([
    [6, 4],
    [8, 6]
])

print("Input matrix is: ")
print(Matrix)

# ------------------------------------------------------------  
# Step 2 : Convert it into flattened layer
# ------------------------------------------------------------  
print(Border)
print("Step 2 : Convert it into flattened layer")
print(Border)

flattened_output = Matrix.flatten()
print("Flattend Output: ")
print(flattened_output)

# ------------------------------------------------------------  
# Step 3 : Final output (FC Layer)
# ------------------------------------------------------------  
print(Border)
print("Step 3 : Final output (FC Layer)")
print(Border)

Weights = np.array([0.1, 0.2, 0.3, 0.4])
Bias = 1

Final_output = np.sum(flattened_output * Weights) + Bias

print("Final output: ")
print(Final_output)

#Flatten layer converts a 2D feature map into a 1D vector so that it can be passed to the Fully Connected (FC) layer for final classification or prediction.