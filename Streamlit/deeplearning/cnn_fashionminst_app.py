import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image, ImageOps

# Load trained model
model = tf.keras.models.load_model("fashion_mnist_model.h5")

# Class labels
class_names = [
    "T-shirt", "Trouser", "Pullover", "Dress", "Coat",
    "Sandal", "Shirt", "Sneaker", "Bag", "Ankle boot"
]

st.title("👕 Fashion MNIST Image Classifier")

st.write("Upload a clothing image (best results with simple images)")

# Upload image
uploaded_file = st.file_uploader("Upload Image", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    # Open image
    image = Image.open(uploaded_file)

    # Show original image
    st.image(image, caption="Original Image", width=250)

    # 🔄 Preprocessing (IMPORTANT FIXES)
    image = image.convert("L")              # Convert to grayscale
    image = ImageOps.invert(image)          # Invert colors
    image = image.resize((28, 28))          # Resize to model input

    st.image(image, caption="Processed Image", width=150)

    # Convert to array
    img_array = np.array(image) / 255.0
    img_array = img_array.reshape(1, 28, 28, 1)

    # Prediction
    prediction = model.predict(img_array)

    predicted_class = np.argmax(prediction)
    confidence = np.max(prediction)

    # Show result
    st.success(f"Predicted: {class_names[predicted_class]}")
    st.info(f"Confidence: {confidence:.2f}")