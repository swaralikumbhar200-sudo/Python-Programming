#Use value_counts() to analyze the distribution of FinalResult.
#Calculate the percentage of Pass and Fail students.
#Is the dataset balanced? Justify your answer.

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

print("Distribution of FinalResult: ")

DistributionOfResult = df["FinalResult"].value_counts()
print("Distribution Result is: ",DistributionOfResult)

NumberofStudents =len(df)
print("Total Students are: ",NumberofStudents)

PassStudents = (df["FinalResult"]==1).sum()
Percentage_PassStudents = (PassStudents/NumberofStudents)*100
print("Percentage of Pass Students: ",Percentage_PassStudents)

FailStudents = (df["FinalResult"]==0).sum()
Percentage_FailStudents = (FailStudents/NumberofStudents)*100
print("Percentage of Fail Students: ",Percentage_FailStudents)


#PassStudent = 60% and FailStudents = 40%
#Dataset is not perfectly balanced but it is not highly imbalanced either





