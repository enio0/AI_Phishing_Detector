# AI-Powered Phishing Detector

A cybersecurity project that uses machine learning to identify
potential phishing emails.

## Project Objectives

- Understand and analyze phishing attacks
- Process datasets of legitimate and phishing emails
- Train a machine learning classification model
- Identify suspicious email characteristics
- Build an interactive web application
- Evaluate detection accuracy and limitations

## Technologies

- Python
- Pandas
- Scikit-learn
- Streamlit
- Joblib

## Project Status

In development.



## Model Evaluation

The phishing detector uses TF-IDF and Logistic Regression.

### Original Dataset: CEAS_08
- Test emails: 7,831
- Accuracy: 99.37%
- False positives: 27
- False negatives: 22

### External Dataset: Nazario_5
- Emails evaluated: 2,844
- Exact training overlaps excluded: 221
- Accuracy: 59.74%
- Suspicious-class precision: 84%
- Suspicious-class recall: 33%
- False negatives: 1,044

### Limitations

The model performs significantly worse on the external dataset.

Potential explanations include differences in email vocabulary,
dataset composition, and labeling conventions.

The original dataset includes spam and suspicious emails, so
classification accuracy does not directly measure real-world
phishing detection performance.

Exact overlapping emails were excluded from external evaluation,
but near-duplicates and shared campaigns have not been ruled out.

The model should not be used as a production security solution.
