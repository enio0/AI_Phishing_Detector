
import streamlit as st
import joblib

from url_analyser import (
    extract_urls,
    check_ip_address,
    check_fake_domain,
    check_at_symbol,
    get_domain
)


# Page
st.set_page_config(
    page_title="AI Phishing Detector",
    page_icon="🛡️",
    layout="centered"
)


# Load our trained model and vectorizer
try:
    model = joblib.load("model.joblib")
    vectorizer = joblib.load("vectorizer.joblib")

except FileNotFoundError:
    st.error("Model files not found. Please run train_model.py first.")
    st.stop()


# Header
st.title("🛡️ AI-Powered Phishing Detector")
st.write("Machine Learning + URL Security Analysis")
st.divider()


# Email input
email = st.text_area(
    "Paste your email below:",
    height=180,
    placeholder="Enter the email content here..."
)


# Analyze button
if st.button("Analyze Email", type="primary"):

    if not email.strip():
        st.warning("Please enter an email.")

    else:
        #convert email text into numbers
        email_tfidf = vectorizer.transform([email])

        #prediction
        prediction = model.predict(email_tfidf)[0]

        #calculate suspicious probability
        probability = model.predict_proba(email_tfidf)[0][1]
        st.subheader("Email Analysis")

        if prediction == 1:
            st.error("Suspicious email detected!")
        else:
            st.success("Email classified as legitimate.")

        st.write(f"Estimated suspicious probability: {probability:.2%}")

        # Probability bar
        st.progress(float(probability))

        st.divider()

        # URL analysis
        st.subheader("URL Security Analysis")

        urls = extract_urls(email)
        warnings_count = 0

        if not urls:
            st.info("No URLs detected.")

        else:
            st.write(f"URLs found: {len(urls)}")

            for url in urls:

                # Display URL without making it clickable
                st.code(url, language=None)
                domain = get_domain(url)
                st.write("Actual destination hostname:", domain)

                # Security checks
                ip_warning = check_ip_address(url)
                fake_warning = check_fake_domain(url)
                at_warning = check_at_symbol(url)

                if ip_warning:
                    st.warning("URL uses an IP address.")
                    warnings_count += 1

                if fake_warning:
                    st.warning("Possible domain impersonation detected.")
                    warnings_count += 1

                if at_warning:
                    st.warning("Misleading @ symbol detected.")
                    warnings_count += 1

                if not ip_warning and not fake_warning and not at_warning:
                    st.info("No suspicious URL patterns detected.")

                st.divider()

        # Security summary
        st.subheader("Security Summary")

        st.metric("URL warning indicators", warnings_count)

        if warnings_count > 0:
            st.warning(
                "Potentially suspicious URL characteristics were found. "
                "Review the email carefully."
            )

        st.caption(
            "The ML prediction and URL checks are independent. "
            "This model was trained on historical spam/suspicious email data. "
            "A low probability or zero URL warnings does not prove an email is safe."
        )
