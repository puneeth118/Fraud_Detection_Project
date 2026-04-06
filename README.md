[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://frauddetectionproject-fed97t7kkm7gyafubnrul.streamlit.app)
# Trustworthy & Interpretable AI for Robust Fraud Detection
Implementation of the Hybrid IAI framework for financial transaction security.

## Project Overview
This project follows the 2025 IEEE research paper to build a fraud detection system that is:
* [cite_start]**Explainable**: Uses Explainable Boosting Machines (EBM) and SHAP so we know *why* a transaction is flagged[cite: 15].
* [cite_start]**Private**: Uses Federated Learning (FL) to train models without sharing raw data between banks[cite: 17].
* [cite_start]**Secure**: Uses Adversarial Training to stay robust against sophisticated hacker attacks[cite: 19].

## My Roadmap
1. [cite_start]**Data Preprocessing**: Cleaning the PaySim/IEEE-CIS datasets[cite: 108].
2. [cite_start]**Model Training**: Building the EBM "Brain"[cite: 113].
3. [cite_start]**Security Testing**: Defending against adversarial patterns[cite: 161].