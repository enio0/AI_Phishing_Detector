import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer

# Load our dataset
df = pd.read_csv("data/CEAS_08.csv")

# Prepare the email text
df["subject"] = df["subject"].fillna("")
df["text"] = df["subject"] + " " + df["body"]

# X contains the emails, y contains the answers
X = df["text"]
y = df["label"]

# Divide our dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

print("Training emails:", len(X_train))
print("Testing emails:", len(X_test))

# Convert email text into numerical features
vectorizer = TfidfVectorizer(max_features=5000)

X_train_tfidf = vectorizer.fit_transform(X_train)
X_test_tfidf = vectorizer.transform(X_test)

print("Training matrix:", X_train_tfidf.shape)
print("Testing matrix:", X_test_tfidf.shape)