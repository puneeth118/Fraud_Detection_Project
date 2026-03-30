import pandas as pd
import shap
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from interpret.glassbox import ExplainableBoostingClassifier
import warnings

# This hides those annoying yellow Mac warnings so your terminal looks clean
warnings.filterwarnings('ignore') 

print("1. Waking up the AI Brain... (Takes about 30 seconds)")
# Loading a smaller 50k sample so the graph generates fast!
df = pd.read_csv('data/paysim dataset.csv').sample(50000, random_state=42)
features = ['oldbalanceOrg', 'step', 'amount', 'newbalanceOrig', 'newbalanceDest']
X = df[features]
y = df['isFraud']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the EBM Brain again
ebm = ExplainableBoostingClassifier(random_state=42)
ebm.fit(X_train, y_train)

print("2. AI Trained! Generating the SHAP Visual Hacker Explanation...")
# We pick 100 random transactions for the AI to "explain"
X_test_sample = X_test.sample(100, random_state=42)

# SHAP looks inside the EBM to see exactly what math it used
explainer = shap.Explainer(ebm.predict, X_train)
shap_values = explainer(X_test_sample)

# Draw the visual graph
plt.figure(figsize=(10, 6))
shap.summary_plot(shap_values, X_test_sample, show=False)
plt.title("SHAP AI Interpretability: How the AI Catches Hackers")
plt.tight_layout()

# Save the graph as a picture!
plt.savefig("AI_Explanation_Graph.png", dpi=300)

print("\n✅ SUCCESS! I just saved a picture of the AI's brain.")
print("Look in your VS Code sidebar for a new file called 'AI_Explanation_Graph.png' and click it!")