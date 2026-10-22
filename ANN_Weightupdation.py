#Write a Python program to show how weights are updated in ANN.
#Tasks:
#1. Take input,weight,bias,target output, and learning rate.
#2. Calculate prediction
#3. Calculate error
#4. Update weight using gradient descent logic
#5. Display old weight and updated weight

input_value = 3
weight = 0.5
bias = 0.2
target = 1
learning_rate = 0.1

#Calculate_prediction 
prediction = input_value * weight + bias

#Calculate Error
Error = target - prediction

#store old weight
old_weight = weight

#update weight
new_weight = old_weight + learning_rate * Error *input_value

print("Prediction: ",prediction)
print("Error: ",Error)
print("Old weight: ",old_weight)
print("Updated weight: ",new_weight)