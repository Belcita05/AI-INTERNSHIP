import streamlit as st
import numpy as np
from sklearn.datasets import load_iris
import joblib

model = joblib.load("svm_model.pkl")
iris = load_iris()

st.title("Iris Flower Classification using SVM")

option = st.selectbox("Select Option", ["Dataset", "Model", "Prediction"])




if option == "Dataset":
    st.write("Features:", iris.feature_names)
    st.write("Classes:", iris.target_names)
    st.write(iris.data[:5])



elif option == "Model":
    st.write("SVM is used for classification.")
    st.write("""Support Vector Machine (SVM) is a supervised machine learning algorithm 
    used for classification. It finds the best boundary (hyperplane) that separates 
    different classes with maximum margin.""")



elif option == "Prediction":
    sl = st.number_input("Sepal Length", 4.0, 8.0)
    sw = st.number_input("Sepal Width", 2.0, 4.5)
    pl = st.number_input("Petal Length", 1.0, 7.0)
    pw = st.number_input("Petal Width", 0.1, 2.5)

    if st.button("Predict"):
        data = np.array([[sl, sw, pl, pw]])
        pred = model.predict(data)

        st.success("Flower: " + iris.target_names[pred][0])