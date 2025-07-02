# 🏦 Loan Eligibility Predictor

This Streamlit web app predicts whether a loan applicant is likely to be approved or not using a machine learning model trained on applicant data such as age, income, credit score, education, and employment status.

---

## 🚀 Features

- Easy-to-use web interface
- Powered by a trained Random Forest classifier
- Predicts loan approval instantly based on your inputs
- Clean layout and mobile-friendly

---

## 📊 How It Works

- The model was trained on a dataset with features like:
  - Age
  - Income
  - Education (Graduate/Not Graduate)
  - Credit Score
  - Marital Status
  - Self-Employed status

- Categorical values were encoded and a Random Forest model was trained to predict loan eligibility.

---

## 🧠 Technologies Used

- Python
- Scikit-learn
- Streamlit
- Pandas, NumPy

---

## ▶️ Run the App Locally

1. Clone this repository
2. Make sure `rf_model.pkl` and `app.py` are in the same folder
3. Install dependencies:

```bash
pip install -r requirements.txt
Run Streamlit:

streamlit run app.py
🌐 Live Demo
➡ Click here to try the live app

📁 Folder Structure
loan-eligibility-predictor/
├── app.py               # Streamlit UI
├── rf_model.pkl         # Trained model file
├── requirements.txt     # Dependencies for Streamlit Cloud
✨ Credits
Created by Anushka Basak
