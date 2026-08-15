#Design machine learning application which follows below steps as:
#Step 1: Get Data
#Load data from MarvellousInfosystems_PlayPredictor.csv file into Python application.

#Step 2: Clean, Prepare and Manipulate Data
#As we want to use the above data into machine learning application we have to prepare that in the format which is accepted by the algorithms.
#As our dataset contains two features as Wether and Temperature. We have to replace each string field into numeric constants by using LabelEncoder from the preprocessing module of sklearn.

#Step 3: Train Data
#Now we want to train our data for that we have to select the Machine Learning algorithm.
#For that we select K Nearest Neighbour (KNN) algorithm. Use the fit() method for training purpose. For training use whole dataset.

#Step 4: Test Data
#After successful training now we can test our trained data by passing some value of weather and temperature.
#As we are using KNN algorithm use value of K as 3.
#After providing the values check the result and display on screen.
#Result may be Yes or No.

#Step 5: Calculate Accuracy
#Write one function as CheckAccuracy() which calculates the accuracy of our algorithm.
#For calculating the accuracy divide the dataset into two equal parts as Training data and Testing data.
#Calculate Accuracy by changing the value of K.

import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

def main():
    #Step1 : Load the dataset:

    Datapath = "MarvellousInfosystems_PlayPredictor.csv"
    df = pd.read_csv(Datapath)
    print("Data loaded Successfully")

    #Step2 : Clean,Prepare and manipulate Data:

    le = LabelEncoder()
    df['Wether'] = le.fit_transform(df['Wether'])
    df['Temperature'] = le.fit_transform(df['Temperature'])
    print(df)

    X = df[['Wether','Temperature']].values
    Y = df['Play']

    print("X shape: ",X.shape)
    print("Y shape: ",Y.shape)

    #Step3 : Train Data:

    model = KNeighborsClassifier(n_neighbors=3)

    model.fit(X,Y)            #whole dataset
    print("Model Trained Successfully")

    #Step4 : Test Data :

    new_point = np.array([[2,1]])

    Y_pred = model.predict(new_point) [0]

    print("Prediction Result is: ",Y_pred)

    CheckAccuracy(X,Y)

def CheckAccuracy(X,Y):
    X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.5,random_state=42)

    for k in range(1,10):
        model = KNeighborsClassifier(n_neighbors=k)

        model.fit(X_train,Y_train)    #dataset divided

        Y_pred = model.predict(X_test)

        Accuracy = accuracy_score(Y_test,Y_pred)        
    
        print("K= ",k,"Accuracy is: ",Accuracy*100 , "%")


if __name__ =="__main__":
    main()
