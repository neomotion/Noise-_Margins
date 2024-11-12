import streamlit as st
import joblib
import numpy as np
import os

# Load the model
model_path = '/home/sahilsssingh5/vlsi/best_xgb_model.joblib'
if os.path.exists(model_path):
    model = joblib.load(model_path)
else:
    st.error("Model file not found. Please check the path.")
    st.stop()

# App title and description
st.title("Noise Margin Prediction")
st.write("Enter the input values to predict the noise margin level:")

# Input fields for user input
Vdd = st.number_input("Vdd", min_value=0.0, max_value=5.0, value=3.3)
Vth = st.number_input("Vth", min_value=0.0, max_value=5.0, value=1.2)
Temperature = st.number_input("Temperature (°C)", min_value=-50.0, max_value=150.0, value=25.0)
Load_Capacitance = st.number_input("Load Capacitance (pF)", min_value=0.0, max_value=100.0, value=10.0)

# Predict button
if st.button("Predict Noise Margin"):
    # Prepare input array
    input_data = np.array([[Vdd, Vth, Temperature, Load_Capacitance]])

    # Prediction
    prediction = model.predict(input_data)

    # Display the prediction result
    if prediction[0] == 0:
        st.write("Prediction: Low Noise Margin")
    else:
        st.write("Prediction: High Noise Margin")
        st.write("""
        ### Tips for Noise Reduction:
        1. **Shield Your Cables:** Use shielded cables to minimize electrostatic noise.
        2. **Use Twisted Pair Cables:** Helps eliminate normal mode noise.
        3. **Isolate Signals:** Prevent ground loops by isolating noisy devices.
        4. **Use Differential Measurements:** Reduces common mode noise and improves signal integrity.
        5. **Ground Wires Properly:** Establish a ground plane for stable reference potential.
        6. **Route Wires Strategically:** Segregate high and low voltage lines to avoid interference.
        7. **Use Anti-Aliasing Filters:** Minimize aliasing and filter high-frequency noise.
        8. **Consider Application-Specific Noise Control:** Consult vendors and follow component instructions to address specific noise sources.
        """)

# To run the app, use: `streamlit run app.py`
