import pandas as pd

# Load the training dataset
df = pd.read_csv("backend/dataset/raw/UNSW_NB15_training-set.csv")

print("Dataset Shape:")
print(df.shape)

print("\nFirst 5 Rows:")
print(df.head())

print("\nColumn Names:")
print(df.columns.tolist())

print("\nMissing Values:")
print(df.isnull().sum())