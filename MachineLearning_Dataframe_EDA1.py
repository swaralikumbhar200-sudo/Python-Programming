#1.Create a DataFrame for student marks and print basic information like shape, columns, and data types.
#data = {
#   'Name': ['Amit', 'Sagar', 'Pooja'],
#    'Math': [85, 90, 78],
#    'Science': [92, 88, 80],
#    'English': [75, 85, 82]
#}

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

Border = "-"*30
Data = {
    'Name': ['Amit', 'Sagar', 'Pooja'],
    'Math': [85, 90, 78],
    'Science': [92, 88, 80],
    'English': [75, 85, 82]
}

df = pd.DataFrame(Data)
print(df)

print("Shape of Dataframe: ",df.shape)
print("Columns in the Dataframe: ",df.columns)
print("Datatypes in the Dataframe: ")
print(df.dtypes)

print(Border)

#2. Use the DataFrame from Q1 and print descriptive statistics using .describe().
print("Statistics of numerical Data: ",df.describe())

print(Border)

#3. Add a new column 'Total' to the DataFrame as the sum of all subject marks.
df['Total'] = df['Math']+ df['Science']+ df['English']
print("New Column 'Total' Added to Dataframe: ",df)

print(Border)

#4. Display students who scored more than 85 in Science.
print("Students who scored more than 85 in science: ")
for i in range(len(df)):
    if df['Science'][i]>85:
        print(df['Name'][i])

print(Border)

#5. Replace 'Pooja' with 'Puja' in the 'Name' column.
df['Name'] = df['Name'].replace('Pooja','Puja')
print("Replaced name 'Pooja' with 'Puja': ")
print(df)

print(Border)

#6. Sort the DataFrame by 'Total' marks in descending order
df = df.sort_values('Total',ascending= False)
print("Total column in Descending order: ")
print(df)

print(Border)

#7. Create a bar plot of student names vs total marks.
print("Bar plot of student names vs total marks: ")
plt.bar(
    df['Name'],
    df['Total'],
    width=0.6,
    linewidth=1,
    edgecolor="black",
    alpha=0.8,
    label ='Students'
)

plt.title("Bar plot of student names vs total marks.")
plt.xlabel('Name of Students')
plt.ylabel('total Marks')
plt.legend()
plt.show()

print(Border)

#8. Plot a line chart of marks for 'Amit' across all subjects.

print("Line Chart of Amit Marks")
subjects = ['Math','Science','English']
marks = [85, 92, 75]

plt.plot(subjects,marks)
plt.xlabel('Subjects')
plt.ylabel('Marks')
plt.title("Amit Marks")
plt.show()

print(Border)

#9. Create a DataFrame with missing values and fill them with column mean.
#data2 = {
#.   'Name': ['Amit', 'Sagar', 'Pooja'],
#    'Math': [np.nan, 76, 88],
#    'Science': [91, np.nan, 85]
#}

Data2 = {
    'Name': ['Amit', 'Sagar', 'Pooja'],
    'Math': [np.nan, 76, 88],
    'Science': [91, np.nan, 85]
}

df2 = pd.DataFrame(Data2)
print("New Dataframe is: ")
print(df2)

mean_math = np.mean(df2['Math'])
df2['Math'] =df2['Math'] .fillna(mean_math)

mean_science = np.mean(df2['Science'])
df2['Science'] =df2['Science'] .fillna(mean_science)

print("Missing Values filled with mean (Math,Science): ")
print(df2)

print(Border)

#10. Drop the 'English' column from original DataFrame.
df = df.drop('English',axis=1)
print("'English' column Dropped from riginal DataFrame: ")
print(df)