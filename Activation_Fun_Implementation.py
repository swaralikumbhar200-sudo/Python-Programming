#Write a Python program to demonstrate different activation functions.
#Functions to implement:
#1.Sigmoid
#2.ReLU
#3.Tanh
#Tasks:
#1.Accept input values from −10 to 10.
#2.Plot all activation functions using Matplotlib.
#3.Explain the use of each activation function.

import numpy as np
import matplotlib.pyplot as plt

#Input Values from -10 to 10
x =np.linspace(-10,10,200)

#Sigmoid function
def Sigmoid(x):
    return 1/(1+np.exp(-x))

def ReLU(x):
    return (np.maximum(0,x))

def tanh(x):
    return np.tanh(x)

#Calculate Output
Sigmoid_output = Sigmoid(x)
ReLU_output = ReLU(x)
tanh_output = tanh(x)

#Plot the all activation functions
plt.plot(x,Sigmoid_output,label="Sigmoid")
plt.plot(x,ReLU_output,label="ReLU")
plt.plot(x,tanh_output,label="Tanh")

plt.xlabel("Input")
plt.ylabel("Output")
plt.title("Activation Functions")
plt.legend()
plt.grid()
plt.show()