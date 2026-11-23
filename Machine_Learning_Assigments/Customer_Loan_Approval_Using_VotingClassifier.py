import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.ensemble import VotingClassifier

Border = "-"*50
#------------------------------------------------------------------
#Step 1 : Load the Dataset
#------------------------------------------------------------------
print(Border)
print("Step 1 : Load the Dataset")
print(Border)

df = pd.read_csv("Customer_Loan_Approval.csv")
print("shape of dataset: ",df.shape)
print("First few records: ")
print(df.head())

#------------------------------------------------------------------
#Step 2 : Check for missing values
#------------------------------------------------------------------
print(Border)
print("Step 2 : Check for missing values")
print(Border)

print("Missing Values are: ")
print(df.isnull().sum())

#------------------------------------------------------------------
#Step 3 : Seperate input and output variables
#------------------------------------------------------------------
print(Border)
print("Step 3 : Seperate input and output variables")
print(Border)

X = df.drop("LoanApproved",axis=1)
Y = df["LoanApproved"]

print("Shape of X: ",X.shape)
print("Shape of Y: ",Y.shape)

#------------------------------------------------------------------
#Step 4 : Split the dataset into training and testing data
#------------------------------------------------------------------
print(Border)
print("Step 4 : Split the dataset into training and testing data")
print(Border)

X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.5,random_state=42)
print("Data Splitted Successfully...")

#---------------------------------------------------------------------
#Step 5 : Scale the features
#---------------------------------------------------------------------
print(Border)
print("Step 5 : Scale the features")
print(Border)

scaler = StandardScaler()

X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

#---------------------------------------------------------------------
#Step 6 : Train model1- Logistic Regression
#---------------------------------------------------------------------
print(Border)
print("Step 6 : Train Train model1- Logistic Regression")
print(Border)

model_log = LogisticRegression(max_iter=1000)

model_log.fit(X_train,Y_train)
print("Model_log Trained Successfully")

Y_pred_log = model_log.predict(X_test)
#---------------------------------------------------------------------
#Step 7 : Train model2- Decision Tree
#---------------------------------------------------------------------
print(Border)
print("Step 7 : Train model2- Decision Tree")
print(Border)

model_Det = DecisionTreeClassifier(max_depth=5,random_state=42)

model_Det.fit(X_train,Y_train)
print("Model_Det Trained Successfully")

Y_pred_Det = model_Det.predict(X_test)
#---------------------------------------------------------------------
#Step 8 : Train model3- KNN
#---------------------------------------------------------------------
print(Border)
print("Step 8 : Train model3- KNN")
print(Border)

model_knn = KNeighborsClassifier(n_neighbors=5)

model_knn.fit(X_train,Y_train)
print("Model_KNN Trained Successfully")

Y_pred_knn = model_knn.predict(X_test)
#---------------------------------------------------------------------
#Step 9 : Accuracy of Three Models
#---------------------------------------------------------------------
print(Border)
print("Step 9 : Accuracy of Three Models")
print(Border)

Accuracy_log = accuracy_score(Y_test,Y_pred_log)
print("Testing Accuracy for logistic_Regression : ",Accuracy_log*100)

Accuracy_Det = accuracy_score(Y_test,Y_pred_Det)
print("Testing Accuracy for Decision_Tree : ",Accuracy_Det*100)

Accuracy_knn = accuracy_score(Y_test,Y_pred_knn)
print("Testing Accuracy for KNN : ",Accuracy_knn*100)

#---------------------------------------------------------------------
#Step 10 : Create Hard voting classifier
#---------------------------------------------------------------------
print(Border)
print("Step 10 : Create Hard voting classifier")
print(Border)

model = VotingClassifier(
    estimators=[
        ('logistic',model_log),
        ('decision_tree',model_Det),
        ('knn',model_knn)
    ],
    voting='hard'
)

model = model.fit(X_train,Y_train)
Y_pred = model.predict(X_test)
print("Model Trained Successfully")
#---------------------------------------------------------------------
#Step 11 : Accuracy of Hard voting classifier
#---------------------------------------------------------------------
print(Border)
print("Step 11 : Accuracy of Hard voting classifier")
print(Border)

Accuracy_Hard = accuracy_score(Y_test,Y_pred)
print("Testing Accuracy for Hard Voting : ",Accuracy_Hard*100)

#---------------------------------------------------------------------
#Step 12 : Create Soft voting classifier
#---------------------------------------------------------------------
print(Border)
print("Step 12 : Create Soft voting classifier")
print(Border)

model = VotingClassifier(
    estimators=[
        ('logistic',model_log),
        ('decision_tree',model_Det),
        ('knn',model_knn)
    ],
    voting='soft'
)

model = model.fit(X_train,Y_train)
Y_pred = model.predict(X_test)
print("Model Trained Successfully")
#---------------------------------------------------------------------
#Step 13 : Accuracy of Soft voting classifier
#---------------------------------------------------------------------
print(Border)
print("Step 13 : Accuracy of Soft voting classifier")
print(Border)

Accuracy_Soft = accuracy_score(Y_test,Y_pred)
print("Testing Accuracy for Soft Voting : ",Accuracy_Soft*100)