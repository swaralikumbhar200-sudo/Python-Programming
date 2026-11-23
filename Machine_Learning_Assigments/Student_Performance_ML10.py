#Plot SleepHours against FinalResult. Does sleeping more guarantee success? Explain.

import pandas as pd
import matplotlib.pyplot as plt

Border = "-"* 30

######################################################################
# Scatterplot of SleepHours vs FinalResult
######################################################################

print(Border)
print("Scatterplot of SleepHours vs FinalResult")
print(Border)

Datapath = "student_performance_ml.csv"

df = pd.read_csv(Datapath)

#Scatterplot

plt.scatter(
    df["SleepHours"],
    df["FinalResult"],
    label = "students",
    marker= "o",
    alpha= 0.8,
    edgecolors="black",
    s=100,
    linewidths=1
)

plt.title("Student Performance Case Study")
plt.xlabel("SleepHours")
plt.ylabel("Final Result")
plt.yticks([0,1])
plt.legend()
plt.show()


#From the graph, students with more sleep generally have better results, but sleep alone is not enough to guarantee success.
#other factors such as study hours, attendance, and assignments can also affect success.