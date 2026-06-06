# Internship Credibility Analyzer
AI-powered internship scam detection and credibility assessment.

## Live Demo 
https://internship-credibility-analyzer-3nd46bjvtkpw8gg9sggme8.streamlit.app/

## Overview

Internship Credibility Analyzer is a Machine Learning-based web application that evaluates internship postings and estimates their credibility.

The system uses Natural Language Processing (TF-IDF) along with handcrafted fraud indicators to identify potentially suspicious internship opportunities and provide a credibility score.

---

## Features

* Internship credibility scoring
* Fraud probability estimation
* Detection of suspicious indicators
* Interactive Streamlit web interface
* Machine Learning powered classification

---

## Technology Stack

* Python
* Scikit-Learn
* TF-IDF Vectorization
* Logistic Regression
* Streamlit
* Pandas
* NumPy
* SciPy

---

## Dataset

The model was trained using internship and job posting data containing both legitimate and fraudulent opportunities.

### Preprocessing Steps

* Data cleaning
* Text normalization
* Feature engineering
* TF-IDF vectorization
* Train-test split

---

## Custom Fraud Indicators

The system evaluates several manually engineered indicators:

* WhatsApp-based applications
* Registration fee requests
* Missing interview process
* Daily earning claims
* Company email presence
* Internship duration mention
* Posting length

---

## Project Structure

internship-credibility-analyzer/

├── app/

│   ├── app.py

│   └── utils.py

│

├── models/

│   ├── fraud_detector.pkl

│   └── tfidf_vectorizer.pkl

│

├── notebooks/

│   ├── EDA_01.ipynb

│   └── Model_02.ipynb

│

├── requirements.txt

├── README.md

└── .gitignore

---

## Installation

Clone the repository:

git clone https://github.com/shristyshreya26/internship-credibility-analyzer.git

cd internship-credibility-analyzer

Install dependencies:

pip install -r requirements.txt

---

## Running the Application

Navigate to the app folder:

cd app

Run Streamlit:

streamlit run app.py

---

## Sample Output

The application provides:

* Credibility Score
* Fraud Probability
* Legitimacy Probability
* Risk Factors

---

## Model Pipeline

1. Data Cleaning and Preprocessing
2. Feature Engineering
3. TF-IDF Vectorization
4. Logistic Regression Classification
5. Credibility Score Generation

---

## Future Improvements

* Transformer-based NLP models (BERT)
* Company verification APIs
* Real-time internship scraping
* Enhanced fraud pattern detection
* Resume-job matching

---

## Author

**Shristy Shreya**
Electronics and Communication Engineering
BIT Mesra
