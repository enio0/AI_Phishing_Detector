
import streamlit as st
import joblib

from url_analyser import (
    extract_urls,
    check_ip_address,
    check_fake_domain,
    check_at_symbol,
    get_domain
)


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

        # Calculate the suspicious email probability
        probability = model.predict_proba(email_tfidf)[0][1]

        # Display email analysis
        st.subheader("Email Analysis")

        if prediction == 1:
            st.error("Suspicious email detected!")
        else:
            st.success("Email classified as legitimate.")

        st.write(
            f"Estimated probability of suspicious email: {probability:.2%}"
        )

        # Extract URLs
        urls = extract_urls(email)

        st.subheader("URL Analysis")

        if not urls:
            st.info("No URLs found in this email.")

        else:
            for url in urls:

                # Display the URL as text, not a clickable link
                st.code(url, language=None)

                # Display the actual destination hostname
                domain = get_domain(url)
                st.write("Actual destination hostname:", domain)

                # Check for suspicious characteristics
                ip_warning = check_ip_address(url)
                fake_domain_warning = check_fake_domain(url)
                at_warning = check_at_symbol(url)

                if ip_warning:
                    st.warning("Warning: This URL uses an IP address.")

                if fake_domain_warning:
                    st.warning(
                        "Warning: Possible domain impersonation detected!"
                    )

                if at_warning:
                    st.warning(
                        "Warning: URL contains an @ symbol in its address!"
                    )

                if not ip_warning and not fake_domain_warning and not at_warning:
                    st.info("No suspicious URL patterns detected.")


st.caption(
    "This model was trained on historical email data. "
    "A legitimate prediction does not guarantee an email is safe."
)
