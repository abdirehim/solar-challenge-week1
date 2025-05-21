import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.set_page_config(page_title="Solar Dashboard", layout="wide")

# === Load data ===
@st.cache_data
def load_data(country):
    path = f"../data/cleaned/{country.lower()}_cleaned.csv"
    df = pd.read_csv(path)
    return df

# === Sidebar controls ===
st.sidebar.title(" Country Selection")
country = st.sidebar.selectbox("Select a Country", ["Benin", "Sierraleone", "Togo"])

df = load_data(country)

# === Main content ===
st.title("🔆 Solar Irradiance Dashboard")
st.subheader(f"Showing data for **{country}**")

st.write("### Summary Statistics")
st.write(df[["GHI", "DNI", "DHI"]].describe())

# Boxplots
st.write("### Distribution of Solar Metrics")
fig, ax = plt.subplots(1, 3, figsize=(15, 4))
sns.boxplot(y=df["GHI"], ax=ax[0])
ax[0].set_title("GHI")
sns.boxplot(y=df["DNI"], ax=ax[1])
ax[1].set_title("DNI")
sns.boxplot(y=df["DHI"], ax=ax[2])
ax[2].set_title("DHI")
st.pyplot(fig)

# Bar chart of average
st.write("### Average Irradiance")
mean_vals = df[["GHI", "DNI", "DHI"]].mean()
st.bar_chart(mean_vals)




