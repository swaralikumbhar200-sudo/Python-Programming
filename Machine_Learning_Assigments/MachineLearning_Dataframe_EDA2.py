#data = {
#   'Name': ['Amit', 'Sagar', 'Pooja'],
#    'Math': [85, 90, 78],
#    'Science': [92, 88, 80],
#    'English': [75, 85, 82]
#}

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler

Border = "-" *40
Data = {
    'Name': ['Amit', 'Sagar', 'Pooja'],
    'Math': [85, 90, 78],
    'Science': [92, 88, 80],
    'English': [75, 85, 82]
}

df = pd.DataFrame(Data)
print(df)

#1. Create a gender column and perform one-hot encoding.
df['Gender'] = ['Male','Male','Female']
df = pd.get_dummies(df,columns=['Gender'],dtype=int)
print(df)

print(Border)

#2. Group students by gender and calculate average marks.
Male = df['Gender_Male'] ==1
print("Average Marks (Male): ")
print(df[Male][['Math','Science','English']].mean())

Female = df['Gender_Female'] ==1
print("Average Marks (Female): ")
print(df[Female][['Math','Science','English']].mean())

print(Border)

#3. Plot a pie chart of subject marks for 'Sagar'.

Subject = ['Math','Science','English']
Marks = [90,88,85]

plt.pie(
    Marks,
    labels=Subject,
    autopct="%1.1f%%"
)

plt.show()

#4. Add a new column 'Status' where students with total >= 250 are 'Pass', else 'Fail'.
df['Total'] =df['Math'] + df['Science'] + df['English']
print("Total (Subjects): ")
print(df['Total'])

df ['Status'] = df['Total'].apply(lambda x :'Pass' if x >=250 else 'Fail')
print(df)

#5. Count how many students passed.
count = (df['Status'] =='Pass').sum()
print("Count of Pass students: ",count)

#6. Export the final DataFrame to a CSV file.
df.to_csv("Final_Students.csv", index = False)

#7. Plot a histogram of Math marks.

Math_Marks = [85, 90, 78]

plt.hist(
    Math_Marks,
    bins = 3,
    edgecolor ="black",
    alpha =0.8,
    rwidth=0.9
)

plt.title("Histogram of Math marks")
plt.show()

#8. Rename 'Math' column to 'Mathematics'.
Rename_math =df.rename(columns={'Math': 'Mathematics'},inplace=True)
print(df)

#9. Plot a boxplot for English marks to check distribution and outliers.
English_Marks = df['English']

plt.boxplot(English_Marks)

plt.title('Distribution of English Marks')
plt.ylabel("English Marks")
plt.show()
#10. Normalize the 'Math' scores using Min-Max scaling.

Scaler =MinMaxScaler()

df['Mathematics']=Scaler.fit_transform(df[['Mathematics']])
print(df)
