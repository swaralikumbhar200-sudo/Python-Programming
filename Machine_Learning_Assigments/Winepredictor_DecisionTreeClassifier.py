import pandas as pd


from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score


Border = "-"* 30

######################################################################
#Step 1 : Load the dataset
######################################################################

print(Border)
print("Step 1 : Load the dataset")
print(Border)

Datapath = "Winepredictor.csv"

df = pd.read_csv(Datapath)

print("Dataset Loaded Successfully.")

print(Border)

######################################################################
#Step 2 : Clean,Prepare and Manipulate Data
######################################################################

print(Border)
print("Step 2 : Clean,Prepare and Manipulate Data ")
print(Border)


print("Shape of the dataset: ",df.shape)
print("Intial Entries are: ")
print(df.head())

print("Data information: ")
df.info()

print("Missing Values per column: ")
print(df.isnull().sum())

print("Statistics of numerical data: ",df.describe())
print("Class Distribution(Count): ")
print(df["Class"].value_counts())

######################################################################
#Step 3 : Decide Independent and Dependent Variables
######################################################################

print(Border)
print("Step 3 : Decide Independent and Dependent Variables")
print(Border)

#X : Independent Variable / Features
#Y : Dependent Variable / Labels

feature_col = [
    "Alcohol","Malic acid","Ash","Alcalinity of ash","Magnesium","Total phenols","Flavanoids",
    "Nonflavanoid phenols","Proanthocyanins","Color intensity","Hue","OD280/OD315 of diluted wines","Proline"
]

X = df[feature_col]
Y = df["Class"]

print("X shape: ",X.shape)
print("Y shape: ",Y.shape)

######################################################################
#Step 4 : Split the Dataset for Training and Testing
######################################################################

print(Border)
print("Step 4 : Split the Dataset for Training and Testing")
print(Border)

X_train ,X_test, Y_train, Y_test = train_test_split(X,Y, test_size= 0.2,random_state=42)

print("Dataset splitting Activity done")

print("X:  ",X.shape)
print("Y: ",Y.shape)

print("X_train: ",X_train.shape)
print("Y_train: ",Y_train.shape)

print("X_test: ",X_test.shape)
print("Y_test: ",Y_test.shape)

######################################################################
#Step 5 : Build the model
######################################################################

print(Border)
print("Step 5 : Build the model")
print(Border)

model = DecisionTreeClassifier()

print("Model gets created Successfully")

######################################################################
#Step 6 : Train the model
######################################################################

print(Border)
print("Step 6 : Train the model")
print(Border)

model.fit(X_train,Y_train)

print("Model Trained Successfully")

######################################################################
#Step 7 : Test the model
######################################################################

print(Border)
print("Step 7 : Test the model")
print(Border)

Y_pred = model.predict(X_test)

print("Model testing Done")

print("Expected Answers: ")
print(Y_test)

print("Predicted Answers: ")
print(Y_pred)

######################################################################
#Step 8 : Accuracy of Model
######################################################################

print(Border)
print("Step 8 : Accuracy of Model")
print(Border)

Accuracy = accuracy_score(Y_test,Y_pred)
print(Accuracy*100)

print(Border)

