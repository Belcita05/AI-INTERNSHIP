import streamlit as st
import pandas as pd
import joblib

model = joblib.load("insurance_model.pkl")
columns = joblib.load("columns.pkl")

st.title("Insurance Cost Prediction")

age = st.slider("Age", 18, 65, 30)
sex = st.selectbox("Sex", ["male", "female"])
bmi = st.number_input("BMI", 10.0, 50.0, 25.0)
children = st.slider("Number of Children", 0, 5, 1)
smoker = st.selectbox("Smoker", ["yes", "no"])
region = st.selectbox("Region", ["northeast", "northwest", "southeast", "southwest"])

# Create DataFrame
input_data = pd.DataFrame([[age, sex, bmi, children, smoker, region]],
                          columns=['age','sex','bmi','children','smoker','region'])

# Encode properly
input_data['sex'] = input_data['sex'].map({'male': 1, 'female': 0})
input_data['smoker'] = input_data['smoker'].map({'yes': 1, 'no': 0})
input_data = pd.get_dummies(input_data)

# Match columns
input_data = input_data.reindex(columns=columns, fill_value=0)

# Prediction
if st.button("Predict Insurance Cost"):
    prediction = model.predict(input_data)
    st.success(f"Estimated Insurance Cost: ₹ {prediction[0]:,.2f}")