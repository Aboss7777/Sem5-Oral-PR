#Program to demonstrate Data Series and Data Frame using Pandas

import pandas as pd
from pandas import Series, DataFrame

# Pandas Series
data = [1, 2, 3, 4, 5, 6, 7, 8]
ser = pd.Series(data)
print("Pandas Series:\n", ser)

#Pandas DataFrame
d = {'Name': pd.Series(['Ayush', 'Pratyush', 'Gaurav', 'Shakunt']),
    'Age': pd.Series([20,25,20,19])}
df = pd.DataFrame(d)
print("\n\nPandas DataFrame:\n", df)
