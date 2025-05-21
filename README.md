
# 🌞 Solar Challenge - Week 1

This repository contains Week 1 work for the 10Academy Solar Challenge. It includes environment setup, exploratory data analysis (EDA) for multiple countries, and a CI pipeline.

---

## Environment Setup

Follow these steps to reproduce the development environment:

### Steps to Reproduce

1. **Clone the repository**
   ```bash
   git clone https://github.com/abdirehim/solar-challenge-week1.git
   cd solar-challenge-week1
Set up virtual environment

On macOS/Linux:

bash
Copy
Edit
python -m venv venv
source venv/bin/activate
On Windows:

bash
Copy
Edit
python -m venv venv
venv\Scripts\activate
Install dependencies

bash
Copy
Edit
pip install -r requirements.txt

CI/CD with GitHub Actions
This repository includes a GitHub Actions workflow to validate the setup automatically.

✅ Defined in .github/workflows/ci.yml

✅ Uses Python 3.11

✅ Runs:

bash
Copy
Edit
pip install -r requirements.txt

Contents
🔹 Task 1: Git & Environment Setup
Set up virtual environment and repo structure

Added .gitignore, requirements.txt, and GitHub Actions CI

🔹 Task 2: Data Profiling, Cleaning & EDA
Summary statistics

Outlier detection

Time series analysis and visualizations for GHI, DNI, DHI

Correlation heatmaps and scatter plots



Submission


data/ folder is excluded from version control

- This repo uses GitHub Actions to automatically check setup with Python 3.11.
