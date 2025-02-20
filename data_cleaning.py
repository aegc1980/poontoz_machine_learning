# data_cleaning.py
import pandas as pd

# Simulate some data that includes duplicates and missing values
data = [
    {"id": 1, "name": "Club One", "loyalty_details": "Basic loyalty program"},
    {"id": 2, "name": "Club Two", "loyalty_details": "Advanced loyalty program"},
    {"id": 2, "name": "Club Two", "loyalty_details": "Advanced loyalty program"},  # duplicate
    {"id": 3, "name": None, "loyalty_details": "Missing club name"}  # missing value
]

df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)

print("\nMissing Values:")
print(df.isnull().sum())

print("\nDuplicate Rows:")
print(df.duplicated())

df_cleaned = df.drop_duplicates()
print("\nDataFrame after removing duplicates:")
print(df_cleaned)

# Fill missing names with a placeholder
df_transformed = df_cleaned.copy()
df_transformed['name'] = df_transformed['name'].fillna("Unknown Club")
df_transformed['id'] = df_transformed['id'].astype(str)

print("\nTransformed DataFrame:")
print(df_transformed)
