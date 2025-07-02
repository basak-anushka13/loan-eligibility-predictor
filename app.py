import streamlit as st
import pandas as pd
import numpy as np
import pickle

# Load model
rf_model = pickle.load(open("rf_model.pkl", "rb"))

# Page config
st.set_page_config(page_title="Loan Eligibility Predictor", page_icon="🏦", layout="centered")

# Sidebar
st.sidebar.image("https://img.icons8.com/dusk/64/bank.png", width=100)
st.sidebar.title("About App")
st.sidebar.markdown("🔮 **Loan Eligibility Predictor**\n\nEnter your details to check whether you're likely to be approved for a loan — powered by a trained machine learning model (Random Forest Classifier).")

# Main Title
st.title("🏦 Loan Eligibility Predictor")
st.markdown("Use this tool to check your **loan approval chances** based on income, education, credit score, and more.")

st.markdown("---")

# Input form using columns
col1, col2 = st.columns(2)

with col1:
    age = st.slider("👤 Age", 21, 60, 30)
    income = st.number_input("💰 Monthly Income (₹)", 10000, 200000, step=1000)
    credit_score = st.slider("📈 Credit Score", 300, 850, 650)

with col2:
    education = st.radio("🎓 Education", ["Graduate", "Not Graduate"])
    married = st.radio("💍 Married?", ["Yes", "No"])
    self_employed = st.radio("💼 Self Employed?", ["Yes", "No"])

# Convert categorical to numeric
education_val = 1 if education == "Graduate" else 0
married_val = 1 if married == "Yes" else 0
self_employed_val = 1 if self_employed == "Yes" else 0

# Prediction
if st.button("🔍 Check Loan Eligibility"):
    input_data = np.array([[age, income, education_val, credit_score, married_val, self_employed_val]])
    prediction = rf_model.predict(input_data)

    st.markdown("---")

    if prediction[0] == 1:
        st.success("✅ **Congratulations!** You're likely to be **approved** for the loan.")
        st.balloons()
    else:
        st.error("❌ **Sorry!** You're **not likely** to be approved. Try improving your credit score or income.")

    st.markdown("📊 *This prediction is made using a trained Random Forest ML model on 1000+ applicant records.*")

st.markdown("---")
st.caption("Made with ❤️ using Streamlit · Model by Anushka")
