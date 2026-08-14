#Write a program to:
#1.Display total number of students in the dataset
#2.Count how many students Passed (FinalResult = 1)
#3.Count how many students Failed (FinalResult = 0)


import pandas as pd

Border = "-"* 30

######################################################################
# Student_Performance
######################################################################

print(Border)
print("Student_Performance")
print(Border)

Datapath = "student_performance_ml.csv"

df = pd.read_csv(Datapath)

print("Total number of students in dataset: ")
print(len(df))

print("Count how many students Passed(FinalResult = 1)")
Count = (df["FinalResult"] == 1).sum()
print(Count)

print("Count how many students Passed(FinalResult = 0)")
Count = (df["FinalResult"] == 0).sum()
print(Count)




