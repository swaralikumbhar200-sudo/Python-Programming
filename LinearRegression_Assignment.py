import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error,r2_score

Border = "-" * 50

######################################################################
#Step 1 : Load the dataset
######################################################################

print(Border)
print("Step 1 : Load the dataset")
print(Border)

Data = "Advertising.csv"
df = pd.read_csv(Data)

print(df.head())
print(Border)

######################################################################
#Step 2 : Clean , Prepare and Manipulate Data
######################################################################

print(Border)
print("Step 2 : Clean , Prepare and Manipulate Data")
print(Border)

#Removing unwanted column:
if "Unnamed: 0" in df.columns:
    df = df.drop(columns=["Unnamed: 0"])
print(df)
print(Border)

#Check missing values:
print("Missing values are(Columns): ")
print(df.isnull().sum())
print(Border)

#Statistical Summary:
print("Statistical Summary is: ")
print(df.describe())
print(Border)

#Correlation
print("Correlation  is: ")
print(df.corr())
print(Border)

######################################################################
#Step 3 : Separate Independent and Dependent Variables
######################################################################

print(Border)
print("Step 3 : Separate Independent and Dependent Variables")
print(Border)

X = df[['TV','radio','newspaper']]
Y = df['sales']

print("X shape: ",X.shape)
print("Y shape: ",Y.shape)

print(Border)

######################################################################
#Step 4 : Train Data
######################################################################

print(Border)
print("Step 4 : Train Data")
print(Border)

X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.5,random_state=42)

print("Data Splitted Successfully")
print(Border)

model = LinearRegression()

model.fit(X_train,Y_train)

print("Model Trained Successfully..")
print(Border)

######################################################################
#Step 5 : Test Data
######################################################################

print(Border)
print("Step 5 : Test Data")
print(Border)

Y_pred = model.predict(X_test)

print("Expected Answer: ")
print(Y_test[:3])

print(Border)

print("Predicted Answer: ")
print(Y_pred[:3])

######################################################################
#Step 6 : Evaluate Data
######################################################################

print(Border)
print("Step 6 : Evaluate Data")
print(Border)

MSE = mean_squared_error(Y_test,Y_pred)

RMSE = np.sqrt(MSE)

R2 = r2_score(Y_test,Y_pred)

print("MSE : ",MSE)
print("RMSE : ",RMSE)
print("R2: ",R2)

print(Border)

#Displaying Coefficients:

print("TV Coefficients: ",model.coef_[0])
print("Radio Coefficients: ",model.coef_[1])
print("Newspaper Coefficients: ",model.coef_[2])

print("Y- intercept is: ",model.intercept_)
print(Border)