# app/utils.py

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def load_clean_data(country: str) -> pd.DataFrame:
    """Load and return cleaned data for the selected country."""
    path = f"../data/cleaned/{country.lower().replace(' ', '')}_cleaned.csv"
    df = pd.read_csv(path)
    return df

def plot_boxplots(df: pd.DataFrame):
    """Return a figure of GHI, DNI, DHI boxplots."""
    fig, ax = plt.subplots(1, 3, figsize=(15, 5))
    sns.boxplot(y=df["GHI"], ax=ax[0], color="#f39c12")
    ax[0].set_title("GHI")
    sns.boxplot(y=df["DNI"], ax=ax[1], color="#27ae60")
    ax[1].set_title("DNI")
    sns.boxplot(y=df["DHI"], ax=ax[2], color="#2980b9")
    ax[2].set_title("DHI")
    return fig

def display_metric_cards(df: pd.DataFrame):
    """Display mean values for GHI, DNI, DHI as Streamlit metrics."""
    ghi = df["GHI"].mean()
    dni = df["DNI"].mean()
    dhi = df["DHI"].mean()
    return ghi, dni, dhi
