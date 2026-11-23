#Write a Python program using StandardScaler to perform feature scaling on the following dataset:
#[[25,20000],[30,40000],[35,80000]]
#Print the scaled dataset.

import pandas as pd
from sklearn.preprocessing import StandardScaler

df = pd.DataFrame([[25,20000],[30,40000],[35,80000]])
print("Values in the Dataset: ")
print(df.to_string(index=False))

scaler = StandardScaler()

df_scaled = pd.DataFrame(scaler.fit_transform(df))

print("Scaled Dataset: ")
print(df_scaled.to_string(index=False))
