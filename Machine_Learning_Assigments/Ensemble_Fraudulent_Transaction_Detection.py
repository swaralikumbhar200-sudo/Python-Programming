import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import BaggingClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import AdaBoostClassifier
from sklearn.ensemble import VotingClassifier

from sklearn.metrics import accuracy_score,precision_score,recall_score,f1_score,confusion_matrix

Border = "-"*50
#------------------------------------------------------------------
#Step 1 : Load the Dataset
#------------------------------------------------------------------
print(Border)
print("Step 1 : Load the Dataset")
print(Border)

df = pd.read_csv("Fraudulent_Transaction_Detection.csv")
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

X = df.drop("Fraud",axis=1)
Y = df["Fraud"]

print("X shape: ",X.shape)
print("Y shape: ",Y.shape)

#------------------------------------------------------------------
#Step 4 : Split the dataset into training and testing data
#------------------------------------------------------------------
print(Border)
print("Step 4 : Split the dataset into training and testing data")
print(Border)

X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.2,random_state=42)
print("Data Splitted Successfully...")

#------------------------------------------------------------------
#Step 5 : Individual Model1 - Decision Tree
#------------------------------------------------------------------
print(Border)
print("Step 5 :  Individual Model1 - Decision Tree")
print(Border)

model_Det = DecisionTreeClassifier(max_depth=5,random_state=42)
model_Det.fit(X_train,Y_train)
Y_pred_Det = model_Det.predict(X_test)

Accuracy_Det = accuracy_score(Y_test,Y_pred_Det)
print("Accuracy of Decision Tree: ",Accuracy_Det*100)

Precision_Det = precision_score(Y_test,Y_pred_Det)
print("Precision of Decision Tree: ",Precision_Det*100)

Recall_Det = recall_score(Y_test,Y_pred_Det)
print("Recall of Decision Tree: ",Recall_Det*100)

F1_Score_Det = f1_score(Y_test,Y_pred_Det)
print("F1 Score of Decision Tree: ",F1_Score_Det*100)

Confusion_Matrix_Det = confusion_matrix(Y_test,Y_pred_Det)
print("Confusion Matrix of Decision Tree: ",Confusion_Matrix_Det)

#------------------------------------------------------------------
#Step 6 : Individual Model2 - Bagging Claasifier
#------------------------------------------------------------------
print(Border)
print("Step 6 : Individual Model2 - Bagging Claasifier")
print(Border)

model_bagging = BaggingClassifier(
    estimator=DecisionTreeClassifier(max_depth=5,random_state=42),
    n_estimators=5,
    random_state=42
)

model_bagging.fit(X_train,Y_train)
Y_pred_bagging = model_bagging.predict(X_test)

Accuracy_bagging = accuracy_score(Y_test,Y_pred_bagging)
print("Accuracy of Bagging Classifier: ",Accuracy_bagging*100)

Precision_bagging = precision_score(Y_test,Y_pred_bagging)
print("Precision of Bagging Classifier: ",Precision_bagging*100)

Recall_bagging = recall_score(Y_test,Y_pred_bagging)
print("Recall of Bagging Classifier: ",Recall_bagging*100)

F1_Score_bagging = f1_score(Y_test,Y_pred_bagging)
print("F1 Score of Bagging Classifier: ",F1_Score_bagging*100)

Confusion_Matrix_bagging = confusion_matrix(Y_test,Y_pred_bagging)
print("Confusion Matrix of Bagging Classifier: ",Confusion_Matrix_bagging)

#------------------------------------------------------------------
#Step 7 : Individual Model3 - Random Forest Claasifier
#------------------------------------------------------------------
print(Border)
print("Step 7 : Individual Model3 - Random Forest Claasifier")
print(Border)

model_Forest = RandomForestClassifier(
    n_estimators=10,
    random_state=42
)
model_Forest.fit(X_train,Y_train)
Y_Pred_Forest = model_Forest.predict(X_test)

Accuracy_Forest = accuracy_score(Y_test,Y_Pred_Forest)
print("Accuracy of Random Forest Classifier: ",Accuracy_Forest*100)

Precision_Forest = precision_score(Y_test,Y_Pred_Forest)
print("Precision of Random Forest Classifier: ",Precision_Forest*100)

Recall_Forest = recall_score(Y_test,Y_Pred_Forest)
print("Recall of Random Forest Classifier: ",Recall_Forest*100)

F1_Score_Forest = f1_score(Y_test,Y_Pred_Forest)
print("F1 Score of Random Forest Classifier: ",F1_Score_Forest*100)

Confusion_Matrix_Forest = confusion_matrix(Y_test,Y_Pred_Forest)
print("Confusion Matrix of Random Forest Classifier: ",Confusion_Matrix_Forest)

#------------------------------------------------------------------
#Step 8 : Individual Model4 - AdaBoost Claasifier
#------------------------------------------------------------------
print(Border)
print("Step 8 : Individual Model4 - AdaBoost Claasifier")
print(Border)

model_AdaBoost = AdaBoostClassifier(
    n_estimators= 50,
    learning_rate=1.0,
    random_state=42
)

model_AdaBoost.fit(X_train,Y_train)
Y_pred_AdaBoost = model_AdaBoost.predict(X_test)

Accuracy_AdaBoost = accuracy_score(Y_test,Y_pred_AdaBoost)
print("Accuracy of AdaBoost Classifier: ",Accuracy_AdaBoost*100)

Precision_AdaBoost = precision_score(Y_test,Y_pred_AdaBoost)
print("Precision of AdaBoost Classifier: ",Precision_AdaBoost*100)

Recall_AdaBoost = recall_score(Y_test,Y_pred_AdaBoost)
print("Recall of AdaBoost Classifier: ",Recall_AdaBoost*100)

F1_Score_AdaBoost = f1_score(Y_test,Y_pred_AdaBoost)
print("F1 Score of AdaBoost Classifier: ",F1_Score_AdaBoost*100)

Confusion_Matrix_AdaBoost = confusion_matrix(Y_test,Y_pred_AdaBoost)
print("Confusion Matrix of AdaBoost Classifier: ",Confusion_Matrix_AdaBoost)

#------------------------------------------------------------------
#Step 9 : Individual Model5 - Voting Claasifier
#------------------------------------------------------------------
print(Border)
print("Step 9 : Individual Model5 - Voting Claasifier")
print(Border)

model = VotingClassifier(
    estimators=[
        ('decision_tree',model_Det),
        ('random forest',model_Forest),
        ('AdaBoost',model_AdaBoost),
        
    ],
    voting='hard'
)

model = model.fit(X_train,Y_train)
Y_pred = model.predict(X_test)



Accuracy_VotingClassifier = accuracy_score(Y_test,Y_pred)
print("Accuracy of Voting Classifier: ",Accuracy_VotingClassifier*100)

Precision_VotingClassifier = precision_score(Y_test,Y_pred)
print("Precision of Voting Classifier: ",Precision_VotingClassifier*100)

Recall_VotingClassifier = recall_score(Y_test,Y_pred)
print("Recall of Voting Classifier: ",Recall_VotingClassifier*100)

F1_Score_VotingClassifier = f1_score(Y_test,Y_pred)
print("F1 Score of Voting Classifier: ",F1_Score_VotingClassifier*100)

Confusion_Matrix_VotingClassifier = confusion_matrix(Y_test,Y_pred)
print("Confusion Matrix of Voting Classifier: ",Confusion_Matrix_VotingClassifier)