
import pandas as pd
import joblib
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# Load the new dataset
df = pd.read_csv("data/Nazario_5.csv")

# Examine its structure
print("DATASET SIZE:")
print(df.shape)

print("\nCOLUMNS:")
print(df.columns)

print("\nLABEL DISTRIBUTION:")
print(df["label"].value_counts())

print("\nMISSING VALUES:")
print(df.isnull().sum())




# Load the original training dataset
original = pd.read_csv("data/CEAS_08.csv")

# Prepare text in both datasets
original["subject"] = original["subject"].fillna("")
df["subject"] = df["subject"].fillna("")

original["text"] = original["subject"] + " " + original["body"]
df["text"] = df["subject"] + " " + df["body"]

# Recreate the original training split
from sklearn.model_selection import train_test_split

X_train, X_test = train_test_split(
    original["text"],
    test_size=0.2,
    random_state=42,
    stratify=original["label"]
)

# Check if external emails were used in training
overlap = set(df["text"]).intersection(set(X_train))

# Remove emails already seen during training
df = df[~df["text"].isin(X_train)]

print("\nEMAILS REMAINING:")
print(len(df))

print("\nEMAILS ALSO FOUND IN TRAINING:")
print(len(overlap))



# Load our previously trained model
model = joblib.load("model.joblib")
vectorizer = joblib.load("vectorizer.joblib")

# Prepare the external dataset
X_external = df["text"]
y_external = df["label"]

# Convert emails into numbers
X_external_tfidf = vectorizer.transform(X_external)

# Make predictions
predictions = model.predict(X_external_tfidf)

# Evaluate the results
print("\nEXTERNAL DATASET ACCURACY:")
print(accuracy_score(y_external, predictions))

print("\nCLASSIFICATION REPORT:")
print(classification_report(y_external, predictions))

print("\nCONFUSION MATRIX:")
print(confusion_matrix(y_external, predictions))


print("\nURL COLUMN DISTRIBUTION:")
print(df["urls"].value_counts())


# Check whether each email contains a URL
has_url = df["text"].str.contains(
    r"https?://", case=False, regex=True
)

# Focus on suspicious-labeled emails
suspicious = y_external == 1

# Calculate detection rates
with_url = suspicious & has_url
without_url = suspicious & ~has_url

print("\nSUSPICIOUS EMAILS WITH URLS:")
print("Total:", with_url.sum())
print("Detected:", (predictions[with_url] == 1).sum())

print("\nSUSPICIOUS EMAILS WITHOUT URLS:")
print("Total:", without_url.sum())
print("Detected:", (predictions[without_url] == 1).sum())