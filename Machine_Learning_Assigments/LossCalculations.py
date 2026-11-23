#Write a Python program to calculate loss manually.
#Tasks:
#1.Implement Mean Squared Error.
#2.Implement Binary Cross Entropy.
#3.Take actual and predicted values.
#4.Display the calculated loss.
#5.Explain which loss function is used for regression and classification.

import numpy as np

#Actual Values
actual = np.array([1,0,1,1])

#Predicted Values
predicted = np.array([0.9,0.2,0.8,0.7])

#Mean Squared Error
def MSE(actual,predicted):
    error = actual-predicted
    squared_error = error ** 2
    return np.mean(squared_error)

#Binary Cross Entropy
def BCE(actual,predicted):
    loss = -(actual * np.log(predicted) + 
            (1 - actual) * np.log(1 - predicted))

    return np.mean(loss)

mse_loss = MSE(actual,predicted)
bce_loss = BCE(actual,predicted)

print("MSE Loss: ",mse_loss)
print("Binary Cross Entropy Loss: ",bce_loss)

#MSE = used for Regression
#Binary cross Entropy = used for binary classification