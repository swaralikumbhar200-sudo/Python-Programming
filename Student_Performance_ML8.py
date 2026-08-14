#Draw a boxplot for Attendance. Identify if any outliers are present.



import pandas as pd

import seaborn as sns

import matplotlib.pyplot as plt

Border = "-"* 30

######################################################################
# Boxplot Histogram of StudyHours
######################################################################

print(Border)
print("Boxplot for attendance")
print(Border)

Datapath = "student_performance_ml.csv"

df = pd.read_csv(Datapath)

#Boxplot 

sns.boxplot(y="Attendance",data=df)

plt.title("Student Performance Case Study")
plt.legend()

plt.show()

#The boxplot shows the distribution of Attendance. There are no visible outliers in the dataset.