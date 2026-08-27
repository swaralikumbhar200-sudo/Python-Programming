#Write a Python program to calculate the Euclidean distance between two points before and after applying feature scaling, and explain the difference in results.
#Points = [[2,1000],[5,5000]]

import numpy as np
from sklearn.preprocessing import StandardScaler

#Dataset
Points = np.array([
    [2,1000],[5,5000]
    ])

Border = "-" * 40
######################################################################
#Euclidean Distance Before feature Scaling
######################################################################

print(Border)
print("Euclidean Distance Before feature Scaling")
print(Border)

Point_A = Points[0]
Point_B = Points[1]

Distance_Before = np.linalg.norm(Point_A-Point_B)

print("Euclidean Distance Before Scaling: ",Distance_Before)

######################################################################
# Feature Scaling
######################################################################

print(Border)
print("Feature Scaling")
print(Border)

scaler = StandardScaler()

scaled_points = scaler.fit_transform(Points)
print("Scaled Points: ")
print(scaled_points)

print(Border)

######################################################################
#Euclidean Distance After feature Scaling
######################################################################

print(Border)
print("Euclidean Distance After feature Scaling")
print(Border)

Scaled_A = scaled_points[0]
Scaled_B = scaled_points[1]

Distance_After = np.linalg.norm(Scaled_A-Scaled_B)

print("Euclidean Distance After Scaling: ",Distance_After)

print(Border)

#Before feature scaling, the feature with larger numerical values has a greater influence on Euclidean distance.
#After feature scaling, the features are brought to a comparable scale, so each feature contributes more fairly to the distance.