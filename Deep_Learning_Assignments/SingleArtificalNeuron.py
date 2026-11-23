#Write a Python program to simulate a single artificial neuron.
#Input:
#x1 = 2
#x2 = 3
#w1 = 0.4
#w2 = 0.6
#bias = 0.5
#Tasks:
#1.Calculate weighted sum.
#2.Apply sigmoid activation function.
#3.Display final output.
#4.Explain whether output is close to 0 or 1.

import numpy as np


#Step1: Input Features
inputs = np.array([2.0,3.0])

#Step2: Weights
Weights = np.array([0.4,0.6])

#Step3: Bias
Bias = 0.5

#Step4: Weighted Sum i.e.Z
#Z = w1x1+w2x2+b
#Z = 2*0.4 + 3*0.6 + 0.5

Z = np.dot(inputs,Weights) +Bias
print("Weighted Sum: ",Z)

#Step5: Activation function:
def Sigmoid(x):
    return 1/(1+ np.exp(-x))

# Step 6 : Final Output
Y = Sigmoid(Z)
print("Y : ",Y)

#Since 0.956 is very close to 1, the neuron produces an output close to 1.