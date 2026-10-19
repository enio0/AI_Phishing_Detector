
import streamlit as st
import joblib

from url_analyser import extract_urls, check_ip_address, check_fake_domain


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

        # Calculate probability of a suspicious email
        probability = model.predict_proba(email_tfidf)[0][1]

        # Display email analysis
        st.subheader("Email Analysis")

        if prediction == 1:
            st.error("Suspicious email detected!")
        else:
            st.success("Email classified as legitimate.")

        st.write(f"Estimated probability of suspicious email: {probability:.2%}")

        # Extract URLs from the email
        urls = extract_urls(email)

        st.subheader("URL Analysis")

        if not urls:
            st.info("No URLs found in this email.")

        else:
            for url in urls:
                st.write("URL:", url)

                # Check for IP address
                if check_ip_address(url):
                    st.warning("Warning: This URL uses an IP address.")

                # Check for domain impersonation
                if check_fake_domain(url):
                    st.warning("Warning: Possible domain impersonation detected!")

                # No suspicious patterns found
                if not check_ip_address(url) and not check_fake_domain(url):
                    st.write("No suspicious URL patterns detected.")


st.caption(
    "This model was trained on historical email data. "
    "A legitimate prediction does not guarantee an email is safe."
)
