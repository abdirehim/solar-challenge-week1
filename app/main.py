# app/main.py

import streamlit as st
import pandas as pd
from utilis import load_clean_data, plot_boxplots, display_metric_cards
import streamlit.components.v1 as components

# --- Page config ---
st.set_page_config(page_title="🔆 Solar Dashboard", layout="wide")

# --- Custom CSS styling ---
st.markdown("""
    <style>
    .main { background-color: #f9f9f9; padding: 20px; }
    h1, h2, h3 { color: #2c3e50; }
    .stMetric {
        background-color: white;
        border-radius: 10px;
        padding: 15px;
        box-shadow: 1px 1px 8px #ccc;
        color: #2c3e50 !important;
    }
    div[data-testid="metric-container"] {
        background-color: #ffffff;
        border-radius: 8px;
        padding: 15px;
        box-shadow: 0 2px 5px rgba(0,0,0,0.1);
        color: #2c3e50 !important;
    }
    div[data-testid="metric-container"] > label {
        color: #7f8c8d !important;
    }
    </style>
""", unsafe_allow_html=True)

# --- Sidebar ---
st.sidebar.title("🌍 Select a Country")
country = st.sidebar.selectbox("Choose Country", ["Benin", "Sierraleone", "Togo"])

# --- Load data ---
df = load_clean_data(country)

# --- Title and Overview ---
st.title(f"☀️ Solar Irradiance Dashboard – {country}")
st.caption("Visual summary of solar potential using cleaned irradiance data.")

# --- Metric Cards ---
ghi, dni, dhi = display_metric_cards(df)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown(f"""
        <div style='background-color:#ffffff; padding:20px; border-radius:10px; box-shadow:0 2px 5px rgba(0,0,0,0.1); text-align:center;'>
            <h4 style='color:#7f8c8d;'>📈 Avg GHI</h4>
            <h2 style='color:#2c3e50;'>{ghi:.2f} W/m²</h2>
        </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
        <div style='background-color:#ffffff; padding:20px; border-radius:10px; box-shadow:0 2px 5px rgba(0,0,0,0.1); text-align:center;'>
            <h4 style='color:#7f8c8d;'>📊 Avg DNI</h4>
            <h2 style='color:#2c3e50;'>{dni:.2f} W/m²</h2>
        </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown(f"""
        <div style='background-color:#ffffff; padding:20px; border-radius:10px; box-shadow:0 2px 5px rgba(0,0,0,0.1); text-align:center;'>
            <h4 style='color:#7f8c8d;'>🌤️ Avg DHI</h4>
            <h2 style='color:#2c3e50;'>{dhi:.2f} W/m²</h2>
        </div>
    """, unsafe_allow_html=True)


st.markdown("---")

# --- Boxplots ---
st.subheader("📦 Distribution of Irradiance Metrics")
fig = plot_boxplots(df)
st.pyplot(fig)

st.subheader("🧮 Correlation Heatmap")
import seaborn as sns
import matplotlib.pyplot as plt

# Only numeric columns
corr_cols = ["GHI", "DNI", "DHI", "Tamb", "TModA", "TModB", "WS", "WSgust", "RH", "BP"]
numeric = df[corr_cols].dropna()

fig, ax = plt.subplots(figsize=(10, 6))
sns.heatmap(numeric.corr(), annot=True, cmap="coolwarm", ax=ax)
st.pyplot(fig)

st.subheader("🫧 Bubble Chart: GHI vs Tamb (Bubble = RH)")

fig, ax = plt.subplots(figsize=(8, 5))
scatter = ax.scatter(
    df["Tamb"], df["GHI"], 
    s=df["RH"] * 1.5,  # bubble size
    alpha=0.6, edgecolors='w', c=df["RH"], cmap="viridis"
)
ax.set_xlabel("Ambient Temperature (Tamb)")
ax.set_ylabel("GHI")
ax.set_title("Bubble Chart of GHI vs Tamb (Size = RH)")
plt.colorbar(scatter, label="Relative Humidity (%)")
st.pyplot(fig)

# --- Time Series Option (Interactive bonus) ---
if st.checkbox("Show Daily GHI Trend"):
    df["Timestamp"] = pd.to_datetime(df["Timestamp"])
    df.set_index("Timestamp", inplace=True)
    daily = df["GHI"].resample("D").mean()
    st.line_chart(daily, use_container_width=True)
