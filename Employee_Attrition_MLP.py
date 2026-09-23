import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score,confusion_matrix

import matplotlib.pyplot as plt

Border = "-"* 30

######################################################################
#Step 1 : Load the dataset
######################################################################

print(Border)
print("Step 1 : Load the dataset")
print(Border)

Datapath = "Employee_Attrition.csv"
df = pd.read_csv(Datapath)

print("Data Loaded Successfully...")

######################################################################
#Step 2 : Clean,Prepare and Manipulate Data
######################################################################

print(Border)
print("Step 2 : Clean,Prepare and Manipulate Data ")
print(Border)

print("Shape of the dataset: ",df.shape)
print("Columns in the dataset: ",df.columns)
print("First five records: ")
print(df.head())

print("Missing Values are: ")
print(df.isnull().sum())

######################################################################
#Step 3 : Identifying numerical and categorical features
######################################################################

print(Border)
print("Step 3 : Identifying numerical and categorical features")
print(Border)

numerical_features = df.select_dtypes(include='number').columns
categorical_features = df.select_dtypes(include='str').columns

print("Numerical features are: ",numerical_features)
print("Categorical features are: ",categorical_features)

######################################################################
#Step 4 : Converting categorical features into numerical features
######################################################################

print(Border)
print("Step 4 : Converting categorical features into numerical features")
print(Border)

le = LabelEncoder()

df['OverTime'] = le.fit_transform(df['OverTime'])
print("OverTime column converted Successfully...")

######################################################################
#Step 5 : Converting Target 'Attrition into 0 and 1
######################################################################

print(Border)
print("Step 5 : Converting Target 'Attrition into 0 and 1")
print(Border)

df['Attrition'] = le.fit_transform(df['Attrition'])

print("First last records: ")
print(df.tail(10))

######################################################################
#Step 6 : Separate independent and dependent variables
######################################################################

print(Border)
print("Step 6 : Separate independent and dependent variables")
print(Border)

X = df.drop('Attrition',axis=1)
Y = df['Attrition']

print("Shape of X: ",X.shape)
print("Shape of Y: ",Y.shape)

######################################################################
#Step 7 : Dividing the dataset into training and testing data
######################################################################

print(Border)
print("Step 7 : Dividing the dataset into training and testing data")
print(Border)

X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.2,random_state=42)

print("Data Spilitted Successfully...")

######################################################################
#Step 8 : Feature Scaling
######################################################################

print(Border)
print("Step 8 : Feature Scaling")
print(Border)

scaler = StandardScaler()
scaled_train = scaler.fit_transform(X_train[numerical_features])
scaled_test = scaler.transform(X_test[numerical_features])

scaled_train_df = pd.DataFrame(
    scaled_train,
    columns=numerical_features,
    index=X_train.index
)

scaled_test_df = pd.DataFrame(
    scaled_test,
    columns=numerical_features,
    index=X_test.index
)

scaled_train_df['OverTime'] = X_train['OverTime']
scaled_test_df['OverTime'] = X_test['OverTime']

print("Scaled Training Data:")
print(scaled_train_df)

print("Scaled Testing Data:")
print(scaled_test_df)

######################################################################
#Step 9 : Creating MLP Classifier
######################################################################

print(Border)
print("Step 9 : Creating MLP Classifier")
print(Border)

model = MLPClassifier(
    hidden_layer_sizes=(2,2),
    activation='relu',
    solver='adam',
    max_iter=1000,
    random_state=42
)

print("Model Created Successfully...")

######################################################################
#Step 10 : Training MLP Classifier
######################################################################

print(Border)
print("Step 10 : Training MLP Classifier")
print(Border)

model.fit(scaled_train_df,Y_train)
print("Model Trained Successfully...")

Y_train_pred = model.predict(scaled_train_df)
Y_test_pred = model.predict(scaled_test_df)


print("Number of iterations required for training: ",model.n_iter_)

######################################################################
#Step 11 : Calculate training and testing accuracy,confusion matrix
######################################################################

print(Border)
print("Step 11 : Calculate training and testing accuracy,confusion matrix")
print(Border)

training_accuracy = accuracy_score(Y_train,Y_train_pred)
print('Training Accuracy is: ',training_accuracy)

testing_accuracy = accuracy_score(Y_test,Y_test_pred)
print("Testing Accuracy is: ",testing_accuracy)

Confusion_matrix = confusion_matrix(Y_test,Y_test_pred)
print("Confusion Matrix: ",Confusion_matrix)

######################################################################
#Step 12 : Plot loss curve
######################################################################

print(Border)
print("Step 12 : Plot loss curve")
print(Border)

plt.plot(model.loss_curve_)
plt.xlabel("Iterations")
plt.ylabel("Loss")
plt.title("MLP Loss Curve")
plt.show()

######################################################################
#Step 13 : Create a function PredictAttrition(employee_data)
######################################################################

print(Border)
print("Step 13 : Create a function PredictAttrition(employee_data)")
print(Border)

def PredictAttrition(employee_data):
    employee_df = pd.DataFrame([employee_data])

    numerical_features=[
        'Age',
        'MonthlyIncome',
        'YearsAtCompany',
        'TotalWorkingYears',
        'DistanceFromHome',
        'JobSatisfaction',
        'WorkLifeBalance',
        'NumCompaniesWorked',
        'TrainingTimesLastYear'
    ]

    employee_scaled = scaler.transform(employee_df[numerical_features])

    employee_scaled_df = pd.DataFrame(
        employee_scaled,
        columns=numerical_features
    )

    employee_scaled_df['OverTime'] = employee_df['OverTime'].values

    prediction = model.predict(employee_scaled_df)

    if prediction[0] == 1:
        return "Attrition: Yes"
    else:
        return "Attrition: No"

######################################################################
#Step 14 : Create 5 new employee record and test it
######################################################################

print(Border)
print("Step 14 : Create 5 new employee record and test it")
print(Border)

employee1 = {
    'Age': 25,
    'MonthlyIncome': 3000,
    'YearsAtCompany': 1,
    'TotalWorkingYears': 2,
    'DistanceFromHome': 10,
    'JobSatisfaction': 2,
    'WorkLifeBalance': 2,
    'NumCompaniesWorked': 3,
    'TrainingTimesLastYear': 2,
    'OverTime': 1
}

employee2 = {
    'Age': 35,
    'MonthlyIncome': 6000,
    'YearsAtCompany': 8,
    'TotalWorkingYears': 12,
    'DistanceFromHome': 5,
    'JobSatisfaction': 4,
    'WorkLifeBalance': 3,
    'NumCompaniesWorked': 2,
    'TrainingTimesLastYear': 3,
    'OverTime': 0
}

employee3 = {
    'Age': 29,
    'MonthlyIncome': 4000,
    'YearsAtCompany': 3,
    'TotalWorkingYears': 5,
    'DistanceFromHome': 20,
    'JobSatisfaction': 2,
    'WorkLifeBalance': 2,
    'NumCompaniesWorked': 4,
    'TrainingTimesLastYear': 2,
    'OverTime': 1
}

employee4 = {
    'Age': 42,
    'MonthlyIncome': 8000,
    'YearsAtCompany': 12,
    'TotalWorkingYears': 18,
    'DistanceFromHome': 3,
    'JobSatisfaction': 4,
    'WorkLifeBalance': 4,
    'NumCompaniesWorked': 1,
    'TrainingTimesLastYear': 4,
    'OverTime': 0
}

employee5 = {
    'Age': 31,
    'MonthlyIncome': 4500,
    'YearsAtCompany': 5,
    'TotalWorkingYears': 8,
    'DistanceFromHome': 15,
    'JobSatisfaction': 3,
    'WorkLifeBalance': 2,
    'NumCompaniesWorked': 3,
    'TrainingTimesLastYear': 3,
    'OverTime': 1
}

print(PredictAttrition(employee1))
print(PredictAttrition(employee2))
print(PredictAttrition(employee3))
print(PredictAttrition(employee4))
print(PredictAttrition(employee5))

######################################################################
#Step 15 : Overfitting or Underfitting
######################################################################

print(Border)
print("Step 15 : Overfitting or Underfitting")
print(Border)

training_accuracy = accuracy_score(Y_train,Y_train_pred)
print('Training Accuracy is: ',training_accuracy)

testing_accuracy = accuracy_score(Y_test,Y_test_pred)
print("Testing Accuracy is: ",testing_accuracy)

if training_accuracy > testing_accuracy + 0.05:
    print("The model is showing signs of overfitting.")

elif training_accuracy < 0.70 and testing_accuracy < 0.70:
    print("The model is showing signs of underfitting.")

else:
    print("The model does not show significant overfitting or underfitting.")