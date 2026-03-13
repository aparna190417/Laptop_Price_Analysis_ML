import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import joblib

# PAGE CONFIG
st.set_page_config(page_title="Laptop Price Dashboard", layout="wide")

st.title("💻 Laptop Price Analysis & Prediction")

# LOAD DATA
df = pd.read_csv("../data/laptop_cleaned.csv")
model = joblib.load("../output/laptop_price_model.pkl")

# KPI SECTION
col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Laptops", len(df))
col2.metric("Average Price (€)", round(df["Price"].mean(),2))
col3.metric("Average RAM", f"{round(df['Ram'].mean(),1)} GB")
col4.metric("Average Weight", f"{round(df['Weight'].mean(),2)} kg")

st.divider()

# VISUALIZATION SECTION
st.subheader("📊 Price Distribution")

fig = px.histogram(
    df,
    x="Price",
    nbins=40,
    color_discrete_sequence=["#5B84B1"]
)

st.plotly_chart(fig, use_container_width=True)

st.subheader("💻 Brand vs Price")

fig2 = px.box(
    df,
    x="Company",
    y="Price",
    color="Company"
)

st.plotly_chart(fig2, use_container_width=True)

st.subheader("⚡ RAM vs Price")

fig3 = px.scatter(
    df,
    x="Ram",
    y="Price",
    color="TypeName"
)

st.plotly_chart(fig3, use_container_width=True)

st.divider()

# PREDICTION SECTION
st.subheader("🤖 Laptop Price Prediction")

company = st.selectbox("Company", sorted(df["Company"].unique()))
product = st.text_input("Product Name")
typename = st.selectbox("Laptop Type", sorted(df["TypeName"].unique()))

ram = st.selectbox("RAM (GB)", sorted(df["Ram"].unique()))
weight = st.slider("Weight (kg)", 1.0, 4.0, 1.5)

screen_inches = st.slider("Screen Size (Inches)", 11.0, 18.0, 13.3)

cpu_company = st.selectbox("CPU Company", sorted(df["CPU_company"].unique()))
cpu_model = st.selectbox("CPU Model", sorted(df["CPU_model"].unique()))
cpu_freq = st.slider("CPU Frequency (GHz)", 1.0, 4.5, 2.5)

gpu_company = st.selectbox("GPU Company", sorted(df["GPU_company"].unique()))
gpu_model = st.selectbox("GPU Model", sorted(df["GPU_model"].unique()))

os = st.selectbox("Operating System", sorted(df["OS"].unique()))

touchscreen = st.selectbox("Touchscreen", ["Yes","No"])
ips = st.selectbox("IPS Panel", ["Yes","No"])
retina = st.selectbox("Retina Display", ["Yes","No"])

primary_storage = st.selectbox("Primary Storage (GB)", sorted(df["PrimaryStorage"].unique()))
primary_type = st.selectbox("Primary Storage Type", sorted(df["PrimaryStorageType"].unique()))

secondary_storage = st.selectbox("Secondary Storage (GB)", sorted(df["SecondaryStorage"].unique()))
secondary_type = st.selectbox("Secondary Storage Type", sorted(df["SecondaryStorageType"].unique()))

ppi = st.slider("PPI", 90, 350, 150)

screen = st.selectbox("Screen Type", sorted(df["Screen"].unique()))

screenW = st.number_input("Screen Width", value=1920)
screenH = st.number_input("Screen Height", value=1080)

# PREDICTION BUTTON
if st.button("Predict Price"):

    # Convert Yes/No to numeric
    touchscreen_val = 1 if touchscreen == "Yes" else 0
    ips_val = 1 if ips == "Yes" else 0
    retina_val = 1 if retina == "Yes" else 0

    input_data = pd.DataFrame({

        "Company":[company],
        "Product":[product],
        "TypeName":[typename],
        "Inches":[float(screen_inches)],
        "Ram":[int(ram)],
        "OS":[os],
        "Weight":[float(weight)],
        "Screen":[screen],
        "ScreenW":[int(screenW)],
        "ScreenH":[int(screenH)],
        "Touchscreen":[touchscreen_val],
        "IPSpanel":[ips_val],
        "RetinaDisplay":[retina_val],
        "CPU_company":[cpu_company],
        "CPU_freq":[float(cpu_freq)],
        "CPU_model":[cpu_model],
        "PrimaryStorage":[int(primary_storage)],
        "SecondaryStorage":[int(secondary_storage)],
        "PrimaryStorageType":[primary_type],
        "SecondaryStorageType":[secondary_type],
        "GPU_company":[gpu_company],
        "GPU_model":[gpu_model],
        "ppi":[float(ppi)]

    })

    prediction = model.predict(input_data)

    # Convert log price to real price
    price = np.exp(prediction)

    st.success(f"Estimated Laptop Price: €{round(price[0],2)}")

    st.balloons()