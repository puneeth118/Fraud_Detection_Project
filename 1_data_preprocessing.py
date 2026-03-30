import pandas as pd
from sklearn.feature_selection import mutual_info_classif
from sklearn.preprocessing import StandardScaler

print("Loading massive PaySim dataset... (This might take a minute on your Mac)")
# Load the transaction data
df = pd.read_csv('data/paysim dataset.csv')
print(f"Data loaded successfully! Total transactions: {len(df):,}")

# Clean up: Select only the math/number columns for our first test
numeric_cols = ['step', 'amount', 'oldbalanceOrg', 'newbalanceOrig', 'oldbalanceDest', 'newbalanceDest']
X = df[numeric_cols]
y = df['isFraud']

# 1. Normalize the features (Required by the paper)
print("\nNormalizing feature scales...")
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# 2. Feature Selection using Mutual Information (MI)
# We use a 10,000 row sample here so it calculates in seconds instead of freezing your 2017 MacBook
print("Calculating Mutual Information to find the best fraud indicators...")
sample_indices = df.sample(10000, random_state=42).index
mi_scores = mutual_info_classif(X_scaled[sample_indices], y.iloc[sample_indices])

# Display the results
mi_results = pd.Series(mi_scores, index=numeric_cols).sort_values(ascending=False)
print("\n--- Top Features for Catching Fraud (MI Scores) ---")
print(mi_results)