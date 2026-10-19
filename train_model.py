
import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# Load dataset
df = pd.read_csv("data/CEAS_08.csv")

# Prepare email text
df["subject"] = df["subject"].fillna("")
df["text"] = df["subject"] + " " + df["body"]

# Features and labels
X = df["text"]
y = df["label"]

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

print("Training emails:", len(X_train))
print("Testing emails:", len(X_test))

# Convert text into numbers
vectorizer = TfidfVectorizer(max_features=5000)

X_train_tfidf = vectorizer.fit_transform(X_train)
X_test_tfidf = vectorizer.transform(X_test)

# Train model
model = LogisticRegression(max_iter=1000)
model.fit(X_train_tfidf, y_train)

# Make predictions
predictions = model.predict(X_test_tfidf)

# Evaluate model
print("\nMODEL ACCURACY:")
print(accuracy_score(y_test, predictions))

print("\nCLASSIFICATION REPORT:")
print(classification_report(y_test, predictions))

print("\nCONFUSION MATRIX:")
print(confusion_matrix(y_test, predictions))

# Check for identical emails across sets
common_emails = set(X_train).intersection(set(X_test))
print("\nIDENTICAL EMAILS IN BOTH SETS:", len(common_emails))

# Save model and vectorizer
joblib.dump(model, "model.joblib")
joblib.dump(vectorizer, "vectorizer.joblib")

print("\nModel and vectorizer saved successfully!")
