import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# ===============================
# 1. Load Dataset
# ===============================
data = pd.read_csv("heart.csv")
print(data.head())

# ===============================
# 2. Input & Output
# ===============================
X = data.drop("Heart_Risk", axis=1)
y = data["Heart_Risk"]

print("\nClass Distribution:")
print(y.value_counts())

print("Input shape:", X.shape)
print("Output shape:", y.shape)

# ===============================
# 3. Train Test Split
# ===============================
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print("Training data:", X_train.shape)
print("Testing data:", X_test.shape)

# ===============================
# 4. Feature Scaling
# ===============================
from sklearn.preprocessing import StandardScaler

sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

print("Data scaled successfully")

# ===============================
# 5. Logistic Regression
# ===============================
from sklearn.linear_model import LogisticRegression

lr_model = LogisticRegression()
lr_model.fit(X_train, y_train)

# ===============================
# 6. Random Forest
# ===============================
from sklearn.ensemble import RandomForestClassifier

rf_model = RandomForestClassifier(n_estimators=150, random_state=42)
rf_model.fit(X_train, y_train)

# ===============================
# 7. XGBoost
# ===============================
from xgboost import XGBClassifier

xgb_model = XGBClassifier(
    n_estimators=200,
    max_depth=5,
    learning_rate=0.1,
    subsample=0.9,
    colsample_bytree=0.9,
    eval_metric="logloss",
    random_state=42
)
xgb_model.fit(X_train, y_train)

# ===============================
# 8. Evaluation
# ===============================
from sklearn.metrics import accuracy_score

lr_pred = lr_model.predict(X_test)
rf_pred = rf_model.predict(X_test)
xgb_pred = xgb_model.predict(X_test)

lr_acc = accuracy_score(y_test, lr_pred)
rf_acc = accuracy_score(y_test, rf_pred)
xgb_acc = accuracy_score(y_test, xgb_pred)

print("\nModel Accuracies")
print("Logistic Regression:", lr_acc * 100)
print("Random Forest:", rf_acc * 100)
print("XGBoost:", xgb_acc * 100)

# ===============================
# 9. Proposed Ensemble Model
# ===============================
from sklearn.ensemble import VotingClassifier

ensemble = VotingClassifier(
    estimators=[
        ('lr', lr_model),
        ('rf', rf_model),
        ('xgb', xgb_model)
    ],
    voting='soft'
)

ensemble.fit(X_train, y_train)

ens_pred = ensemble.predict(X_test)
ens_acc = accuracy_score(y_test, ens_pred)

print("\nProposed Ensemble Accuracy:", ens_acc * 100)

# ===============================
# 10. New Patient Prediction
# ===============================
new_patient = np.array([[1, 1, 0, 1, 0, 1, 120, 200, 1, 0, 1, 0, 0, 1, 0, 1, 55, 1]])
new_patient = sc.transform(new_patient)

prediction = ensemble.predict(new_patient)

if prediction[0] == 1:
    print("\n⚠️ Heart Disease Detected")
else:
    print("\n✅ No Heart Disease")

# ===============================
# 11. Save Models & Scaler
# ===============================
import pickle

print("\nSaving trained models...")

# Save ensemble model
with open('heart_model.pkl', 'wb') as f:
    pickle.dump(ensemble, f)
print("✓ Ensemble model saved as heart_model.pkl")

# Save scaler
with open('scaler.pkl', 'wb') as f:
    pickle.dump(sc, f)
print("✓ Scaler saved as scaler.pkl")

# ===============================
# 12. Explainable AI using SHAP
# ===============================
import shap

print("\nGenerating SHAP explanations...")

# Create SHAP explainer for XGBoost
explainer = shap.Explainer(xgb_model, X_train[:100])  # Use subset for speed
print("✓ SHAP explainer created successfully")
