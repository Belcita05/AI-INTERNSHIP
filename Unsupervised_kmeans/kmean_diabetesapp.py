import streamlit as st
import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.datasets import load_diabetes
import joblib

# Load dataset
kmeans = joblib.load("kmeans_model.pkl")
diabetes= load_diabetes()

# Select features
features = ['Glucose', 'BMI', 'Age']
X = df[features]

# Scale data
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Train KMeans
kmeans = KMeans(n_clusters=2, random_state=42)
kmeans.fit(X_scaled)

# UI
st.title(" Diabetes Patient Clustering (K-Means)")
st.write("Enter patient details:")

# Inputs
glucose = st.number_input("Glucose Level", value=120)
bmi = st.number_input("BMI", value=25.0)
age = st.number_input("Age", value=30)

# Predict
if st.button("Predict Cluster"):
    input_data = np.array([[glucose, bmi, age]])
    
    # Scale input
    input_scaled = scaler.transform(input_data)
    
    # Predict cluster
    cluster = kmeans.predict(input_scaled)
    
    if cluster[0] == 0:
        st.success("Cluster 0: Lower Risk Pattern Group")
    else:
        st.success("Cluster 1: Higher Risk Pattern Group")

# Optional: Show dataset preview
if st.checkbox("Show Dataset"):
    st.write(df.head())