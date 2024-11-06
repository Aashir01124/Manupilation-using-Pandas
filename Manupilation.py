import pandas as pd
import numpy as np

data = {
    'Id': [1, 2, 3, 4],
    'Name': ['Pankaj', 'Meghna', 'David', 'Lisa'],
    'Role': [np.nan, 'CEO', np.nan, np.nan],
    'Salary': [100, 200, np.nan, np.nan]
}

df = pd.DataFrame(data)

print("First 2 and last 2 rows of the DataFrame:")
print(pd.concat([df.head(2), df.tail(2)]))

total_nulls = df.isnull().sum().sum()
print("\nTotal number of null values in the DataFrame:", total_nulls)

print("\nDetailed information of the DataFrame:")
print(df.info())

df_no_null_rows = df.dropna()
print("\nDataFrame after dropping rows with null values:")
print(df_no_null_rows)

df_no_null_columns = df.dropna(axis=1)
print("\nDataFrame after dropping columns with null values:")
print(df_no_null_columns)

df['Salary'].fillna(300, inplace=True)
print("\nDataFrame after filling null values in Salary column with 300:")
print(df)

df['Role'].fillna('CEO', inplace=True)
print("\nDataFrame after filling null values in Role column with 'CEO':")
print(df)