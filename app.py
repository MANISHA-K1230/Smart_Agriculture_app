import streamlit as st
import joblib
import numpy as np
import os

st.set_page_config(
    page_title="AI-Powered Smart Agriculture: Intelligent Crop Recommendation System",
    page_icon="🌾",
    layout="wide"
)

# Load trained model
model = joblib.load("model/crop_model.pkl")

# Crop prices
crop_prices = {
    "rice": 2200,
    "maize": 1800,
    "wheat": 2100,
    "cotton": 7000,
    "millet": 2500,
    "sugarcane": 3000
}

# Local crop images (inside images folder)
crop_images = {
    "rice": "images/rice.jpg",
    "maize": "images/maize.jpg",
    "wheat": "images/wheat.jpg",
    "cotton": "images/cotton.jpeg",
    "millet": "images/Millets.jpg",
    "sugarcane": "images/sugarcane.jpg"
}

# UI Styling
st.markdown("""
<style>
.stApp{
background-image: url("https://images.unsplash.com/photo-1500937386664-56d1dfef3854");
background-size: cover;
background-position: center;
}

.block-container{
background: rgba(255,255,255,0.90);
padding: 2rem;
border-radius: 20px;
}

.title{
font-size:50px;
font-weight:bold;
text-align:center;
color:#1b4332;
}

.metric-box{
background:white;
padding:20px;
border-radius:15px;
box-shadow:0 4px 15px rgba(0,0,0,0.15);
text-align:center;
}

.result-box{
background:#2d6a4f;
padding:25px;
border-radius:20px;
color:white;
font-size:25px;
font-weight:bold;
}
.stSlider > div > div > div > div {
    background-color: skyblue;
}
.stSlider [role="slider"]{
background-color:skyblue;
}
</style>
""", unsafe_allow_html=True)

# Title
st.markdown('<div class="title">🌾 AI-Powered Smart Agriculture: Intelligent Crop Recommendation System</div>', unsafe_allow_html=True)

# Sidebar inputs
st.sidebar.title("Farm Inputs")

N = st.sidebar.slider("Nitrogen", 0, 150)
P = st.sidebar.slider("Phosphorus", 0, 150)
K = st.sidebar.slider("Potassium", 0, 150)
temperature = st.sidebar.slider("Temperature", 0, 50)
humidity = st.sidebar.slider("Humidity", 0, 100)
ph = st.sidebar.slider("Soil pH", 0.0, 14.0, 6.5)
rainfall = st.sidebar.slider("Rainfall", 0, 300)

# Dashboard cards
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown(
        f'<div class="metric-box">🌡 Temperature<br><h2>{temperature}°C</h2></div>',
        unsafe_allow_html=True
    )

with col2:
    st.markdown(
        f'<div class="metric-box">💧 Humidity<br><h2>{humidity}%</h2></div>',
        unsafe_allow_html=True
    )

with col3:
    st.markdown(
        f'<div class="metric-box">🌧 Rainfall<br><h2>{rainfall} mm</h2></div>',
        unsafe_allow_html=True
    )

with col4:
    st.markdown(
        f'<div class="metric-box">🧪 Soil pH<br><h2>{ph}</h2></div>',
        unsafe_allow_html=True
    )

# Prediction
if st.button("Predict Best Crop"):
    data = np.array([[N, P, K, temperature, humidity, ph, rainfall]])

    crop = model.predict(data)[0]
    profit = crop_prices.get(crop, 0)

    # Result
    st.markdown(
        f'<div class="result-box">Recommended Crop: {crop}<br>Expected Profit: ₹{profit}</div>',
        unsafe_allow_html=True
    )

    # Crop Preview
    st.subheader("Crop Preview")

    if crop in crop_images:
        image_path = crop_images[crop]

        if os.path.exists(image_path):
            st.image(
                image_path,
                caption=f"{crop} cultivation preview",
                use_container_width=True
            )
        else:
            st.error(f"Image not found: {image_path}")
    else:
        st.warning("Crop image not available")

    # Soil nutrients
    st.subheader("Soil Nutrient Status")

    c1, c2, c3 = st.columns(3)

    c1.metric("Nitrogen", N)
    c2.metric("Phosphorus", P)
    c3.metric("Potassium", K)

    # Water requirement
    st.subheader("Water Requirement")
    water_score = min(rainfall, 100)
    st.progress(water_score)

    # Best season
    st.subheader("Best Season")

    season_map = {
        "rice": "Monsoon",
        "wheat": "Winter",
        "maize": "Winter",
        "cotton": "Summer",
        "millet": "Summer",
        "sugarcane": "Monsoon"
    }

    st.success(season_map.get(crop, "Season data unavailable"))

    # Irrigation advice
    st.subheader("Irrigation Advice")

    if rainfall < 80:
        st.warning("Extra irrigation required")
    elif rainfall < 150:
        st.info("Moderate irrigation required")
    else:
        st.success("Rainfall sufficient")

    # Soil tips
    st.subheader("Soil Improvement Tips")

    if ph < 5.5:
        st.warning("Soil acidic → Add lime")
    elif ph > 7.5:
        st.warning("Soil alkaline → Add gypsum")
    else:
        st.success("Soil pH balanced")

    # Pest risk
    st.subheader("Pest Risk")

    if humidity > 75:
        st.error("High pest risk")
    else:
        st.success("Low pest risk")

    # Yield prediction
    st.subheader("Estimated Yield")

    yield_estimate = (N + P + K) * 2
    st.info(f"Expected Yield: {yield_estimate} kg/acre")

    # Market demand
    st.subheader("Market Demand")

    high_demand = ["rice", "cotton", "sugarcane"]

    if crop in high_demand:
        st.success("High market demand")
    else:
        st.info("Normal market demand")

    # Fertilizer suggestions
    st.subheader("Fertilizer Suggestions")

    if N < 50:
        st.warning("Increase Nitrogen fertilizer")

    if P < 50:
        st.warning("Increase Phosphorus fertilizer")

    if K < 50:
        st.warning("Increase Potassium fertilizer")

    # Crop rotation
    st.subheader("Crop Rotation Recommendation")

    rotation = {
        "rice": "Pulses",
        "wheat": "Corn",
        "cotton": "Groundnut",
        "maize": "Soybean"
    }

    next_crop = rotation.get(crop, "Pulses")
    st.success(f"Next season recommended crop: {next_crop}")