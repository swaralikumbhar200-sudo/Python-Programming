#Write a Python program to load the file student_performance_ml.csv using pandas. Display:
#1.First 5 records
#2.Last 5 records
#3.Total number of rows and columns
#4.List of column names
#5.Data types of each column

import pandas as pd


Border = "-"* 30

######################################################################
# Student_Performance
######################################################################

print(Border)
print("Student_Performance")
print(Border)

DataPath = "student_performance_ml.csv"

df = pd.read_csv(DataPath)

print("First 5 records are: ")
print(df.head(5))

print("Last 5 records are: ")
print(df.tail(5))

print("Total number of rows and columns:")
print(df.shape)

print("List of column names: ")
print(list(df.columns))

print("Data types of each column: ")
print(list(df.dtypes))