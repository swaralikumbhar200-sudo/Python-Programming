#Create a neural network model to predict whether a customer will leave a service.
#Features:
#Age,Monthly charges,Tenure,Number of complaints,Customer support calls
#0 = Customer will stay
#1 = Customer will leave
#Tasks:
#1.Load or create dataset.
#2.Clean the dataset.
#3.Apply StandardScaler.
#4.Train FNN model.
#5.Evaluate accuracy.
#6. Predict approva; for new applicant

import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier

#----------------------------------------------------------------------
# Step 1 : Dataset Creation:
#----------------------------------------------------------------------

Border = "-" * 40
print(Border)
print("Step 1 : Dataset Creation:")
print(Border)

X = np.array([
    [25, 500, 12, 1, 2],
    [30, 700, 24, 0, 1],
    [45, 1200, 6, 5, 8],
    [50, 1500, 5, 6, 10],
    [28, 600, 18, 1, 1],
    [35, 800, 30, 0, 0],
    [48, 1400, 4, 7, 9],
    [52, 1600, 3, 8, 12],
    [27, 550, 20, 0, 1],
    [42, 1300, 8, 4, 7]
])

y = np.array([
    0, 0, 1, 1, 0,
    0, 1, 1, 0, 1
])

print("Dataset Created Successfully...")

#----------------------------------------------------------------------
# Step 2 : Clean the Dataset
#----------------------------------------------------------------------
print(Border)
print("Step 2 : Clean the Dataset")
print(Border)

X = pd.DataFrame(
    X,
     columns= ["Age" , "Monthly charges","Tenure","Complaints","Support Calls"]
)

y = pd.DataFrame(y,columns=["Churn"])

print("Features are: ")
print(X)
print("Labels are: ")
print(y)

#----------------------------------------------------------------------
# Step 3 : Apply StandardScaler
#----------------------------------------------------------------------
print(Border)
print("Step 3 : Apply StandardScaler")
print(Border)

scaler = StandardScaler()

X_scaled = scaler.fit_transform(X)

print("After scaling features")
print(X_scaled)

#----------------------------------------------------------------------
# Step 4 : Train FNN model
#----------------------------------------------------------------------
print(Border)
print("Step 4 : Train FNN model")
print(Border)

model = MLPClassifier(
    hidden_layer_sizes=(10,),
    activation='relu',
    solver='adam',
    max_iter=1000,
    random_state=42
)

model.fit(X,y)
print("Model Trained Successfully")

#----------------------------------------------------------------------
# Step 5 : Evaluate Accuracy
#----------------------------------------------------------------------
print(Border)
print("Step 5 : Evaluate Accuracy")
print(Border)

new_customer = pd.DataFrame(
    [[46,1450,5,6,9]],
     columns= ["Age" , "Monthly charges","Tenure","Complaints","Support Calls"]
)

new_customer_scaled = scaler.transform(new_customer)

prediction = model.predict(new_customer_scaled)

if prediction == 1:
    print("Prediction: Customer may leave")
else:
    print("Prediction: Customer may stay")
    