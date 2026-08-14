#Based on the dataset values, analyze whether:
#1.Higher StudyHours increase the chance of passing.
#2.Higher Attendance improves FinalResult.
#Write your observations in 4–5 lines.

import pandas as pd

Border = "-"* 30

######################################################################
# StudyHours vs Chance of Passing
######################################################################

print(Border)
print("StudyHours vs Chance of Passing")
print(Border)

Datapath = "student_performance_ml.csv"

df = pd.read_csv(Datapath)

PassData = df[df["FinalResult"]==1]
Number_PassStudents = len(PassData)
print("Number of Pass Students: ",Number_PassStudents)

Studyhrs_Pass = PassData["StudyHours"].sum()
print("Study Hours of Pass Students: ",Studyhrs_Pass)

Average_StudyHrs_Pass = Studyhrs_Pass/Number_PassStudents
print("Average of Study Hours of Pass Students: ",Average_StudyHrs_Pass)

print(Border)

FailData = df[df["FinalResult"]==0]
Number_FailStudents = len(FailData)
print("Number of Fail Students: ",Number_FailStudents)

Studyhrs_Fail = FailData["StudyHours"].sum()
print("Study Hours of Fail Students: ",Studyhrs_Fail)

Average_StudyHrs_Fail = Studyhrs_Fail/Number_FailStudents
print("Average of Study Hours of Fail Students: ",Average_StudyHrs_Fail)

print(Border)

print("Higher StudyHours increase the change of passing is proved")

print(Border)

Border = "-"* 30

#Pass students have higher study hours than failed students.so it conclude that higher studyhrs may increase the chance of passing

######################################################################
# Attendance improves Final Result
######################################################################

print(Border)
print("Attendance improves Final Result")
print(Border)

PassData = df[df["FinalResult"]==1]
Number_PassStudents = len(PassData)
print("Number of Pass Students: ",Number_PassStudents)

Attendance_Pass = PassData["Attendance"].sum()
print("Attendance of Pass Students: ",Attendance_Pass)

Average_Attendane_Pass = Attendance_Pass/Number_PassStudents
print("Average Attendance of Pass Students: " ,Average_Attendane_Pass)

print(Border)

FailData = df[df["FinalResult"]==0]
Number_FailStudents = len(FailData)
print("Number of Fail Students: ",Number_FailStudents)

Attendance_Fail = FailData["Attendance"].sum()
print("Attendance of Fail Students: ",Attendance_Fail)

Average_Attendane_Fail = Attendance_Fail/Number_FailStudents
print("Average Attendance of Fail Students: " ,Average_Attendane_Fail)

print(Border)

#Pass students have an average study time of 6.37 hours, while fail students have an average of 2.55 hours.
#This shows that higher StudyHours are associated with a higher chance of passing.
#Pass students have an average attendance of 86.61%, compared to 67.75% for fail students.
#Therefore, higher attendance is also associated with better FinalResult.