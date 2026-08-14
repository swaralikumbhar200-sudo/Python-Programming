#Using pandas functions, calculate and display:
#1.Average StudyHours
#2.Average Attendance
#3.Maximum PreviousScore
#4.Minimum SleepHours

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

print("Average StudyHours: ")
TotalStudyHours = (df["StudyHours"].sum())
NumberOfStudents = len(df)
AverageStudyHours = (TotalStudyHours/NumberOfStudents)
print(AverageStudyHours)

print("Average Attendance: ")
TotalAttendance = (df["Attendance"].sum())
NumberOfStudents = len(df)
AverageAttendance = (TotalAttendance/NumberOfStudents)
print(AverageAttendance)

print("Maximum PreviousScore: ")
print(df["PreviousScore"].max())

print("Minumum SleepHours: ")
print(df["SleepHours"].min())