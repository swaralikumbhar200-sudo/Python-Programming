#Use KNN to predict whether a student passes or fails based on study hours and attendance.
#Tasks
#1.Accept input from the user:
#2.Study hours
#3.Attendance percentage
#4.Apply the KNN algorithm.
#5.Predict whether the student Passes or Fails.


import numpy as np
from sklearn.neighbors import KNeighborsClassifier

X = np.array([
    [2, 60],
    [5, 80],
    [6, 85],
    [1, 50]
])

Y = np.array(["Fail", "Pass", "Pass", "Fail"])


# Accepting input from user for StudyHours and Attendance:

new_study_hours = float(input("Enter Study Hours: "))
new_attendance = float(input("Enter Attendance: "))

new_point = np.array([[new_study_hours,new_attendance]])


#Create KNN Algorithm

model = KNeighborsClassifier(n_neighbors=3)

#fit model

model.fit(X,Y)

#Prediction

Prediction = model.predict(new_point)
print("Predicted Result is: ",Prediction[0])