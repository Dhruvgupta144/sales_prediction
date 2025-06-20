import pickle as pk
import streamlit as st

# Title
st.title("📊 Advertising Sales Predictor")
st.write("Hello! I am Dhruv Gupta and this is my Advertising Sales Prediction App.")

# Load model
with open("advertising_model.pkl", 'rb') as f:
    model = pk.load(f)

# User inputs
st.header("Enter Advertising Budgets")

tv_budget = st.number_input('TV Budget (in thousands of dollars)', min_value=0.0, value=100.0, step=1.0)
radio_budget = st.number_input('Radio Budget (in thousands of dollars)', min_value=0.0, value=20.0, step=1.0)
newspaper_budget = st.number_input('Newspaper Budget (in thousands of dollars)', min_value=0.0, value=10.0, step=1.0)

# Predict button
if st.button('Predict Sales'):
    input_data = [[tv_budget, radio_budget, newspaper_budget]]
    prediction = model.predict(input_data)
    st.write(f"🛒 Predicted Sales: **{prediction[0]:.2f}k units**")
