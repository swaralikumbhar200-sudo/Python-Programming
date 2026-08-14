#Plot a histogram of StudyHours.
#Explain what the distribution tells you.

import pandas as pd

import matplotlib.pyplot as plt



Border = "-"* 30

######################################################################
# Plot Histogram of StudyHours
######################################################################

print(Border)
print("Histogram of StudyHours")
print(Border)

Datapath = "student_performance_ml.csv"

df = pd.read_csv(Datapath)


#Histogram Plot

plt.hist(
    df["StudyHours"],
    bins= 5,
    edgecolor="black",
    alpha = 0.8,
    rwidth=0.9
)

plt.title("Distribution of Study Hours")
plt.xlabel("Study Hours")
plt.ylabel("Number of Students")
plt.show()

#here in above histogram:
#1.The study hours are distributed from around 1 to 8 hours.
#2.Most students are studying between 1–2, 4–5, 5–6, and 6–7 hours.
#3.The highest number of students is in the 7–8 hours range, with about 7 students.