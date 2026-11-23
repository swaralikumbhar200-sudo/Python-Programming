#Write a Python program that calculates TP, TN, FP, FN for the following arrays:
#actual    = [1, 1, 1, 1, 0, 0, 0, 0]
#predicted = [1, 1, 0, 1, 0, 1, 0, 0]
#Display all four values.

#Display the complete classification report including precision, recall, F1-score, and support.

import numpy as np
from sklearn.metrics import classification_report

Border = "-" * 40

######################################################################
#Calculation of TP, TN, FP, FN
######################################################################

print(Border)
print("Calculation of TP, TN, FP, FN")
print(Border)


actual = np.array([1, 1, 1, 1, 0, 0, 0, 0])
predicted = np.array([1, 1, 0, 1, 0, 1, 0, 0])

TP = np.sum((actual ==1) &(predicted==1))
TN = np.sum((actual ==0) &(predicted==0))
FP = np.sum((actual ==0) &(predicted==1))
FN = np.sum((actual ==1) &(predicted==0))

print("True Positive (TP):", TP)
print("True Negative (TN):", TN)
print("False Positive (FP):", FP)
print("False Negative (FN):", FN)

######################################################################
#Classification Report
######################################################################

print(Border)
print("Classification Report")
print(Border)

print("Classification Report is: ")
print(classification_report(actual,predicted))