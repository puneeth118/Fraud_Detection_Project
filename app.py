import streamlit as st
import pandas as pd
from interpret.glassbox import ExplainableBoostingClassifier
import warnings

warnings.filterwarnings('ignore')

# 1. Setup the Webpage
st.set_page_config(page_title="IAI Fraud Defender", layout="centered")
st.title("🛡️ IAI Fraud Detection System")
st.write("Enter a financial transaction below. The Explainable AI will scan it for adversarial patterns.")

# 2. Train a lightweight "Web AI" instantly
@st.cache_resource
def load_web_ai():
    # We use a tiny hardcoded dataset so the web app deploys instantly without the 500MB file
    X_train = pd.DataFrame({
        'oldbalanceOrg': [1000, 500000, 200, 400000, 50], 
        'step': [1, 1, 2, 1, 3], 
        'amount': [50, 500000, 20, 5000, 10], 
        'newbalanceOrig': [950, 0, 180, 395000, 40], 
        'newbalanceDest': [50, 500000, 20, 5000, 10]
    })
    y_train = pd.Series([0, 1, 0, 1, 0]) # 1 = Hacker, 0 = Safe
    
    ebm = ExplainableBoostingClassifier(random_state=42)
    ebm.fit(X_train, y_train)
    return ebm

ai_brain = load_web_ai()

# 3. Build the User Interface Form
st.markdown("### 🔍 Transaction Scanner")
col1, col2 = st.columns(2)

with col1:
    old_balance = st.number_input("Sender's Original Balance ($)", value=500000)
    amount = st.number_input("Amount to Transfer ($)", value=5000)

with col2:
    new_balance = st.number_input("Sender's New Balance ($)", value=495000)
    dest_balance = st.number_input("Receiver's New Balance ($)", value=5000)

# 4. The "Scan" Button
if st.button("🚨 Scan Transaction"):
    # Package the user's input
    user_data = pd.DataFrame({
        'oldbalanceOrg': [old_balance], 'step': [1], 'amount': [amount],
        'newbalanceOrig': [new_balance], 'newbalanceDest': [dest_balance]
    })
    
    # AI makes a prediction
    prediction = ai_brain.predict(user_data)[0]
    
    st.markdown("---")
    if prediction == 1:
        st.error("### ❌ FRAUD DETECTED: Transaction Blocked!")
        st.write("The Interpretable AI flagged this as a highly suspicious adversarial pattern.")
    else:
        st.success("### ✅ TRANSACTION APPROVED: Safe")
        st.write("No suspicious activity detected.")