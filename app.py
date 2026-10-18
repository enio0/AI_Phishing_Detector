import streamlit as st
import joblib

# Load our trained model and vectorizer
model = joblib.load("model.joblib")
vectorizer = joblib.load("vectorizer.joblib")

# Application title
st.title("AI-Powered Phishing Detector")

st.write("Paste an email below to check if it is suspicious.")

# Email input
email = st.text_area("Email content")

# Analyze button
if st.button("Analyze Email"):

    if email.strip() == "":
        st.warning("Please enter an email.")

    else:
        # Convert email text into numbers
        email_tfidf = vectorizer.transform([email])

        # Predict the email category
        prediction = model.predict(email_tfidf)[0]

        # Calculate the probability of a suspicious email
        probability = model.predict_proba(email_tfidf)[0][1]

        # Display the result
        if prediction == 1:
            st.error("Suspicious email detected!")
        else:
            st.success("Email classified as legitimate.")

        # Display probability
        st.write(f"Estimated probability of suspicious email: {probability:.2%}")

st.caption("This model was trained on historical email data. A legitimate prediction does not guarantee an email is safe.")