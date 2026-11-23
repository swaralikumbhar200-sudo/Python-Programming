#Write a python program to manually perform convolution.
# Input : A 5x5 matrix representing grayscale image.
# Kernel : A 3x3 edge detection filter.
# Tasks : 1. Move kernel over image. 2. Perform multiplication and addition. 3. Generate feature map. 4.Print each region calculation.

import numpy as np

Border = "-" * 30
# ------------------------------------------------------------  
# Step 1 :  5x5 Input Image Matrix  
# ------------------------------------------------------------  
print(Border)
print("Step 1 :  5x5 Input Image Matrix")
print(Border)

image = np.array([
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]
])
print("Original 5x5 Image: ")
print(image)

# ------------------------------------------------------------  
# Step 2 : 3x3 Kernel for Edge Detection 
# ------------------------------------------------------------  
print(Border)
print("Step 2 : 3x3 Kernel for Edge Detection ")
print(Border)

kernel = np.array([
    [-1, -1, -1],
    [0, 0, 0],
    [1, 1, 1]
])

print("3*3 Kernel: ")
print(kernel)

# ------------------------------------------------------------  
# Step 3 : Convolution Operation  
# Output Size = (5-3+1) x (5-3+1) = 3x3  
# ------------------------------------------------------------ 
print(Border)
print("Step 3 : Convolution Operation")
print(Border)

Feature_map =np.zeros((3,3))

for i in range(3):
    for j in range(3):
        region = image[i:i+3,j:j+3]
        result = np.sum(region * kernel)

        Feature_map[i][j] = result
        print("Region at: ",i,j)
        print(region)

        print("Multiplication: ")
        print(region * kernel)

        print("Result: ",result)

# ------------------------------------------------------------  
# Step 4 : Show Feature Map  
# ------------------------------------------------------------  
print(Border)
print("Step 4 : Show Feature Map  ")
print(Border)

print("Feature Map (Detected Edge)")  
print(Feature_map)  


