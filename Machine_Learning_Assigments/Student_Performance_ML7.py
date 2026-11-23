#Create a scatter plot of:
#StudyHours vs PreviousScore
#Use different colors for Pass and Fail students.

import pandas as pd

import matplotlib.pyplot as plt
import seaborn 


Border = "-"* 30

######################################################################
# Plot Histogram of StudyHours
######################################################################

print(Border)
print("Histogram of StudyHours")
print(Border)

Datapath = "student_performance_ml.csv"

df = pd.read_csv(Datapath)

PassData = df[df["FinalResult"] == 1]
FailData = df[df["FinalResult"] == 0]

#Scatter plot
plt.scatter(
    PassData["StudyHours"],
    PassData["PreviousScore"],
    s=100,
    marker='o',
    alpha=0.8,
    edgecolors='black',
    linewidths=1,
    color='green',
    label='Pass'
)

plt.scatter(
    FailData["StudyHours"],
    FailData["PreviousScore"],
    s=100,
    marker='o',
    alpha=0.8,
    edgecolors='black',
    linewidths=1,
    color='red',
    label='Fail'
)
plt.title("Student Performance Case Study")

plt.xlabel("Study Hours")
plt.ylabel("Previous Score")

plt.legend()
plt.grid()
plt.show()