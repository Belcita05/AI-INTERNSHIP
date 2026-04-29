import streamlit as st
import joblib
import numpy as np

# Load model
model = joblib.load("ecommerce_model.pkl")

# Title
st.title("Spending Prediction App")

# Simple inputs
session = st.number_input("Session Length")
app_time = st.number_input("Time on App")
website_time = st.number_input("Time on Website")
membership = st.number_input("Membership")

# Predict
if st.button("Predict"):
    data = np.array([[session, app_time, website_time, membership]])
    prediction = model.predict(data)

    st.write(f"Predicted Spending: ₹ {prediction[0]:.2f}")