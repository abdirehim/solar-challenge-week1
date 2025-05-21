---

## 🧪 Development Process

This Streamlit dashboard was developed as part of **Task 4: Interactive Dashboard** in the 10Academy Solar Challenge. The objective was to visualize solar irradiance data interactively and present key insights across countries.

### Key Steps:
1. **Data Preparation**
   - Cleaned CSVs generated in previous EDA steps (`benin_clean.csv`, `togo_clean.csv`, `sierraleone_clean.csv`).
   - Saved in `data/` directory and excluded from version control via `.gitignore`.

2. **Dashboard Setup**
   - Created `app/` directory with `main.py` as the Streamlit entry point.
   - Added `utils.py` to modularize key logic (e.g., data loading, plotting).

3. **Visualizations**
   - Metric cards showing average GHI, DNI, DHI
   - Boxplots to show irradiance distribution
   - Correlation heatmap across environmental variables
   - Bubble chart of GHI vs Tamb (bubble size = RH)
   - Optional time series chart (GHI daily trend)

4. **UI Styling**
   - Custom CSS applied for modern card designs and layout polish.

5. **Version Control**
   - Dashboard developed in `dashboard-dev` branch and merged via Pull Request to `main`.

---

## ▶️ Usage Instructions

### 🧩 Prerequisites

Ensure the following are installed:

- Python 3.11
- All dependencies in `requirements.txt` (especially Streamlit, pandas, seaborn, matplotlib)

Install them using:
```bash
pip install -r requirements.txt

---

## 🌐 Live Dashboard

The solar data dashboard is deployed and publicly accessible at:

👉 [https://solar-challenge-week1-edb4sxejtehrqxn6czndcg.streamlit.app/](https://solar-challenge-week1-edb4sxejtehrqxn6czndcg.streamlit.app/)

> Use the dropdown to select a country and view interactive visualizations of solar irradiance (GHI, DNI, DHI), correlation insights, and environmental effects.

---

## 🧪 Development Process

This app was built using [Streamlit](https://streamlit.io/) and follows modular coding practices. Key features include:

- 📈 Average irradiance cards (GHI, DNI, DHI)
- 📦 Boxplots showing distribution
- 🧮 Correlation heatmap across environmental variables
- 🫧 Bubble chart (GHI vs Tamb, size = RH)
- 📅 Daily GHI trend toggle

See [Usage Instructions](#-usage-instructions) to run the app locally.

---


