import pandas as pd

# Load the dataset
df = pd.read_csv("data/CEAS_08.csv")

# Basic information
print("\nDATASET SIZE:")
print(df.shape)

print("\nCOLUMNS:")
print(df.columns)

print("\nEMAIL DISTRIBUTION:")
print(df["label"].value_counts())

print("\nMISSING VALUES:")
print(df.isnull().sum())

# Prepare email text
df["subject"] = df["subject"].fillna("")
df["text"] = df["subject"] + " " + df["body"]

# Check duplicate email content
print("\nDUPLICATE EMAILS:")
print(df.duplicated(subset=["text"]).sum())