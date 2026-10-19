# AI-Powered Phishing Detector

A cybersecurity project combining **Machine Learning** and **rule-based URL security analysis** to identify potentially suspicious emails.

Built with Python, Scikit-learn, and Streamlit.

**Status:** Experimental cybersecurity prototype developed for educational and portfolio purposes. Not intended for production use.

## Project Overview

Phishing is a cyberattack in which attackers impersonate trusted organizations or individuals to trick victims into revealing sensitive information or performing harmful actions.

This project explores how machine learning and traditional cybersecurity techniques can work together to identify suspicious emails.

The system consists of two independent components:

1. **Machine Learning Classifier:** Analyzes email text using TF-IDF and Logistic Regression.
2. **URL Security Analyzer:** Examines links for suspicious characteristics, including IP addresses, misleading domains, and URL user-information tricks.

An interactive Streamlit dashboard presents the results.

## Features

### Machine Learning

- Email classification (legitimate or suspicious)
- TF-IDF text feature extraction
- Logistic Regression classification
- Estimated suspicious-email probability
- Visual probability indicator

### URL Security Analysis

- URL extraction from email content
- Detection of IP-address-based URLs
- Basic domain impersonation detection
- Detection of common typosquatting patterns
- Detection of misleading `@` symbols
- Actual destination hostname identification
- Summary of detected URL warning indicators

### Application

- Interactive Streamlit dashboard
- Clear warnings and classification results
- Basic error handling for missing model files
- Automated URL security tests

## Technologies Used

| Technology | Purpose |
|------------|---------|
| Python | Main programming language |
| Pandas | Dataset processing and exploration |
| Scikit-learn | Machine learning and evaluation |
| TF-IDF | Converting email text into numerical features |
| Logistic Regression | Email classification |
| Streamlit | Interactive web application |
| Joblib | Model serialization |
| unittest | Automated testing |
| Git & GitHub | Version control |

## How It Works

1. The user submits an email through the Streamlit application.
2. The email text is transformed into numerical features using a trained TF-IDF vectorizer.
3. A Logistic Regression classifier predicts whether the email resembles legitimate or suspicious messages.
4. The application displays the model's estimated suspicious-class probability.
5. The URL analyzer extracts HTTP and HTTPS links.
6. Rule-based security checks analyze their structure and hostnames.
7. The dashboard displays URL warnings alongside the independent machine learning prediction.

**Important:** The machine learning prediction and URL analysis are separate. URL warnings do not currently modify the model's probability.

## Project Structure

```text
AI_Phishing_Detector/
├── app.py
├── train_model.py
├── evaluate_model.py
├── explore_data.py
├── url_analyser.py
├── test_analyzer.py
├── requirements.txt
├── README.md
├── .gitignore
├── data/
│   ├── CEAS_08.csv
│   └── Nazario_5.csv
├── model.joblib
└── vectorizer.joblib
```

The `data/` folder and `.joblib` files are stored locally and excluded from GitHub.

## Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/enio0/AI_Phishing_Detector.git
cd AI_Phishing_Detector
```

### 2. Create a virtual environment

On Linux/macOS:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

On Windows (PowerShell):

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
python -m pip install -r requirements.txt
```

The project uses:

- pandas
- scikit-learn
- streamlit
- joblib

### 4. Download the dataset

Download `CEAS_08.csv` from:

https://zenodo.org/records/8339691

Create a folder named `data` in the project directory and place the CSV file inside it.

Expected location:

```text
data/CEAS_08.csv
```

### 5. Train the machine learning model

Run:

```bash
python train_model.py
```

This will:

- Load the dataset
- Prepare the email text
- Split the data into training and testing sets
- Apply TF-IDF feature extraction
- Train the Logistic Regression classifier
- Evaluate the model
- Save the trained model and vectorizer

Two files will be generated:

```text
model.joblib
vectorizer.joblib
```

### 6. Run the application

```bash
python -m streamlit run app.py
```

Open the local address displayed in the terminal, usually:

http://localhost:8501

### 7. Run automated tests

```bash
python -m unittest test_analyzer.py -v
```

The test suite checks the behavior of URL extraction and security analysis functions.

## Model Evaluation

The model was evaluated on its original dataset and a separate email collection.

### Original Dataset — CEAS_08

| Metric | Result |
|--------|--------|
| Total emails | 39,154 |
| Training emails | 31,323 |
| Testing emails | 7,831 |
| Accuracy | 99.37% |
| False positives | 27 |
| False negatives | 22 |

The model performed extremely well on the original random test split.

However, these results do not establish real-world phishing detection accuracy.

### External Dataset — Nazario_5

To investigate generalization, the saved model was tested on a second dataset without retraining.

Exact text overlaps with the original training split were excluded.

| Metric | Result |
|--------|--------|
| Initial emails | 3,065 |
| Excluded overlapping emails | 221 |
| Evaluated emails | 2,844 |
| Accuracy | 59.74% |
| Suspicious-class precision | 83.76% |
| Suspicious-class recall | 33.29% |
| False positives | 101 |
| False negatives | 1,044 |

### Key Findings

The model's accuracy decreased from **99.37%** on its original test set to **59.74%** on the external dataset.

This significant drop suggests limited generalization between the two email collections.

Possible causes include:

- Differences in email vocabulary and formatting
- Differences in dataset composition
- Historical spam patterns learned during training
- Differences in labeling conventions
- Distribution shift between the datasets

The external evaluation excluded exact training-text overlaps, but near-duplicates and shared campaigns have not been fully investigated.

These results demonstrate why external validation is essential when evaluating machine learning security systems.

## External Evaluation Instructions

Download `Nazario_5.csv` from:

https://zenodo.org/records/8339691

Place it inside:

```text
data/Nazario_5.csv
```

First, train the original model if you have not already done so:

```bash
python train_model.py
```

Then run:

```bash
python evaluate_model.py
```

The evaluation script:

1. Loads the external dataset.
2. Recreates the original training split to identify exact email-text overlaps.
3. Excludes overlapping examples.
4. Loads the saved model and TF-IDF vectorizer.
5. Makes predictions without retraining.
6. Reports classification performance.

## Automated Security Tests

The project includes automated tests using Python's built-in `unittest` framework.

The tests cover:

- URL extraction
- IP address detection
- Domain impersonation patterns
- Common typosquatting patterns
- Misleading `@` symbols
- Actual hostname extraction
- URL punctuation handling
- Uppercase hostname handling
- Multiple URL extraction
- Combined security indicators

Run the tests using:

```bash
python -m unittest test_analyzer.py -v
```

The current suite contains 11 tests.

Passing these tests verifies expected behavior for the included cases, not comprehensive URL security coverage.

## Limitations

This application is an experimental prototype and has several important limitations:

1. **Historical training data:** The original dataset contains older spam and suspicious-email examples, not exclusively confirmed phishing attacks.
2. **Limited generalization:** External evaluation showed substantially lower accuracy and recall.
3. **Possible dataset overlap:** Exact training overlaps were removed, but similar messages may remain.
4. **Basic URL heuristics:** The analyzer recognizes selected suspicious patterns but cannot detect every malicious URL.
5. **No domain reputation verification:** The application does not check threat intelligence databases or verify domain ownership.
6. **Uncalibrated probabilities:** Model probabilities should not be interpreted as verified real-world phishing risk.
7. **No attachment analysis:** Email attachments are not inspected.
8. **Limited email metadata analysis:** Sender authentication, SPF, DKIM, and DMARC are not currently evaluated.

A classification of "legitimate" does not guarantee that an email is safe.

## Security Considerations

- Never open suspicious URLs found in email datasets.
- Do not load untrusted `.joblib` model files.
- Do not upload private emails, credentials, or sensitive datasets to GitHub.
- Treat submitted email content as untrusted input.
- Do not rely on the application's results as the sole basis for security decisions.

## Dataset Source

**Phishing Email Curated Datasets**

Zenodo:

https://zenodo.org/records/8339691

The datasets are not included in this repository.

## Future Improvements

- Evaluate on newer phishing-specific datasets
- Investigate near-duplicate messages and shared campaigns
- Improve URL parsing and registered-domain detection
- Expand typosquatting and brand impersonation detection
- Compare Logistic Regression with other ML algorithms
- Investigate calibrated probability estimates
- Add email-header authentication analysis
- Integrate appropriate threat intelligence sources
- Improve robustness against adversarial phishing examples

## Project Purpose

This project was developed as part of an independent cybersecurity learning journey.

Its goal is to demonstrate practical understanding of:

- Machine learning for security applications
- Email phishing and spam classification
- URL security analysis
- Data preprocessing and model evaluation
- Automated software testing
- Python application development
- Git and GitHub version control

The emphasis is on understanding the techniques, evaluating their limitations, and developing practical cybersecurity engineering skills.

## Disclaimer

This project is intended for educational and research purposes only.

It is not a production-ready phishing detection solution.