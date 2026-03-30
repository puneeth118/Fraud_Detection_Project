import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from interpret.glassbox import ExplainableBoostingClassifier

print("Loading a sample of the PaySim data...")
# We load a random sample so your Mac processes it quickly
df = pd.read_csv('data/paysim dataset.csv').sample(100000, random_state=42)

# We use the top fraud-catching features we discovered in Phase 2
features = ['oldbalanceOrg', 'step', 'amount', 'newbalanceOrig', 'newbalanceDest']
X = df[features]
y = df['isFraud']

# Split the data: 80% to train the AI, 20% to test it like an exam
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print("\nTraining the Explainable Boosting Machine (EBM)...")
print("This is the 'Brain' of your AI. It might take 1-2 minutes...")

# Initialize and train the EBM (The exact model from your paper!)
ebm = ExplainableBoostingClassifier(random_state=42)
ebm.fit(X_train, y_train)

print("\nModel trained successfully! 🧠")

# Test the model on the 20% of data it hasn't seen yet
print("Testing the model on unseen transaction data...\n")
predictions = ebm.predict(X_test)

print("--- AI Hacker Detection Report ---")
# This prints out the accuracy, precision, and recall
print(classification_report(y_test, predictions, zero_division=0))