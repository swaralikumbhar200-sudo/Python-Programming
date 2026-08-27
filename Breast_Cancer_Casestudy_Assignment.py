import pandas as pd

from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_breast_cancer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix,classification_report,accuracy_score

import matplotlib.pyplot as plt
import seaborn as sns

Border = "-"* 40

######################################################################
#Breast Cancer Prediction
######################################################################
print(Border)
print("Breast Cancer Prediction")
print(Border)

######################################################################
#Step 1 : Load the dataset
######################################################################
print(Border)
print("Step 1 : Load the dataset")
print(Border)

data = load_breast_cancer()

df = pd.DataFrame(data.data, columns=data.feature_names)
df["Target"] = data.target

print("First Values from Dataset: ")
print(df.head())

print(Border)

######################################################################
#Step 2 : Data Preprocessing
######################################################################
print(Border)
print("Step 2 : Data Preprocessing")
print(Border)

print("Missing values are: ")
print(df.isnull().sum())

#scale features:
X = df.drop("Target",axis=1)
Y = df["Target"]

scaler = StandardScaler()

scaled_features =scaler.fit_transform(X)

print("Scaled Features: ")
print(scaled_features)

print(Border)

######################################################################
#Step 3 : Exploratory Data Analysis (EDA)
######################################################################
print(Border)
print("Step 3 : Exploratory Data Analysis (EDA)")
print(Border)

print("Summary Statistics: ")
print(df.describe())

print("Visualization of Feature Correlations")
Correlation = df.corr()

plt.figure(figsize=(12, 8))
sns.heatmap(Correlation)
plt.show()

######################################################################
#Step 4 : Split the Dataset
######################################################################
print(Border)
print("Step 4 : Split the Dataset")
print(Border)

X_train,X_test,Y_train,Y_test = train_test_split(scaled_features,Y,test_size=0.2,random_state=42)

print("Data Splitted Successfully...")
print(Border)

######################################################################
#Step 5 : Building the Model
######################################################################
print(Border)
print("Step 5 : Building the Model")
print(Border)

model = LogisticRegression()

model.fit(X_train,Y_train)
print("Model Trained Successfully...")

Y_pred = model.predict(X_test)

Predicted_Tumor_Types = data.target_names[Y_pred]
Actual_Tumor_Types = data.target_names[Y_test]

print("Predicted Tumor Types:")
print(Predicted_Tumor_Types)

print("Actual Tumor Types:")
print(Actual_Tumor_Types)

print(Border)

######################################################################
#Step 6 : Evaluation of Model
######################################################################
print(Border)
print("Step 6 : Evaluation of Model")
print(Border)

accuracy = accuracy_score(Y_test,Y_pred)
print("Accuracy is : ",accuracy)

Confusion_matrix = confusion_matrix(Y_test,Y_pred)
print("Confusion Matrix is : ",Confusion_matrix)

Classification_report = classification_report(Y_test,Y_pred)
print("Classification Report is: ")
print(Classification_report)

######################################################################
#Step 7 : Observations and Conclusion
######################################################################

print(Border)
print("Step 7 : Observations and Conclusion")
print(Border)

print("The Logistic Regression model was used to predict tumor type.")
print("The model was evaluated using accuracy, confusion matrix,")
print("precision, recall and F1-score.")
print("The model achieved good classification performance on the test data.")