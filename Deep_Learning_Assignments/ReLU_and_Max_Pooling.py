#Write a python program to demonstrate ReLU and Max Pooling
#Tasks : 1. Create a feature map with positive and negative values. 2. Apply ReLU.  3. Apply 2x2 max pooling.  4. Display output after each step.  5. Explain why pooling reduces size

import numpy as np

Border = "-" * 30
# ------------------------------------------------------------  
# Step 1 :  Feature Map
# ------------------------------------------------------------  
print(Border)
print("Step 1 :  Feature Map")
print(Border)

Feature_map = np.array([
    [3, 3 , 3],
    [0, 0, 0],
    [-3, -3, -3]
])

print("Feature map is: ")
print(Feature_map)

# ------------------------------------------------------------  
# Step 2 :  Apply ReLU
# ------------------------------------------------------------  
print(Border)
print("Step 2 :  Apply ReLU")
print(Border)

Relu_output = np.maximum(0,Feature_map)
print(Relu_output)

# ------------------------------------------------------------  
# Step 3 :  Apply 2x2 max pooling
# ------------------------------------------------------------  
print(Border)
print("Step 3 :  Apply 2x2 max pooling")
print(Border)

Max_pooling_output = np.zeros((2,2))

for i in range(2):
    for j in range(2):

        region = Relu_output[i:i+2,j:j+2]
        result = np.max(region)

        Max_pooling_output[i][j]= result
        print("Output after: ",i,j)
        print(result)

print("Max pooling output is: ")
print(Max_pooling_output) 

#Pooling reduces the size because it keeps only one value from multiple values in each small region. As a result, the number of values in the feature map decreases.
# This reduces computation and memory usage while preserving important features.
