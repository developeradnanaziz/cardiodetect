"""
Heart Disease Prediction - Model Training Pipeline
UCI Heart Disease Dataset
Target: Heart Disease Prediction (Binary Classification)
"""

import numpy as np
import pandas as pd
import joblib
import warnings
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier
from sklearn.ensemble import VotingClassifier
from sklearn.metrics import (
    accuracy_score, precision_score, recall_score, f1_score, 
    roc_auc_score, confusion_matrix, classification_report, roc_curve, auc
)
from imblearn.over_sampling import SMOTE
import matplotlib.pyplot as plt

warnings.filterwarnings('ignore')

# ===============================
# Configuration
# ===============================
DATASET_PATH = 'heart.csv'
MODEL_SAVE_PATH = 'heart_model.pkl'
SCALER_SAVE_PATH = 'scaler.pkl'
RANDOM_STATE = 42
TEST_SIZE = 0.2

print("=" * 80)
print("HEART DISEASE PREDICTION MODEL - TRAINING PIPELINE")
print("=" * 80)

# ===============================
# Step 1: Load Dataset
# ===============================
print("\n[1/7] Loading dataset...")
try:
    df = pd.read_csv(DATASET_PATH)
    print(f"✓ Dataset loaded: {df.shape[0]} samples, {df.shape[1]} features")
    print(f"First few rows:\n{df.head()}")
    print(f"\nDataset Info:\n{df.info()}")
except FileNotFoundError:
    print(f"✗ Error: {DATASET_PATH} not found!")
    exit(1)

# ===============================
# Step 2: Data Preprocessing
# ===============================
print("\n[2/7] Data Preprocessing...")

# Identify target column (assumes 'target' or heart disease related column)
# The dataset uses different column names, so we'll handle this intelligently
target_col = None
for col in df.columns:
    if 'target' in col.lower() or 'heart' in col.lower() or 'risk' in col.lower():
        target_col = col
        break

if target_col is None:
    # Assume last column is target
    target_col = df.columns[-1]

print(f"✓ Target column identified: '{target_col}'")

X = df.drop(columns=[target_col])
y = df[target_col]

print(f"Features shape: {X.shape}")
print(f"Target shape: {y.shape}")
print(f"Class distribution:\n{y.value_counts()}")
print(f"Class balance: {y.value_counts(normalize=True)}")

# Handle missing values
print("\nHandling missing values...")
missing_before = X.isnull().sum().sum()
X = X.fillna(X.mean())
missing_after = X.isnull().sum().sum()
print(f"✓ Missing values before: {missing_before}, after: {missing_after}")

# Feature names for later use
feature_names = X.columns.tolist()
print(f"✓ Features: {feature_names}")

# ===============================
# Step 3: Train-Test Split
# ===============================
print("\n[3/7] Splitting data into train-test sets...")
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=TEST_SIZE, random_state=RANDOM_STATE, stratify=y
)
print(f"✓ Training set: {X_train.shape[0]} samples")
print(f"✓ Testing set: {X_test.shape[0]} samples")
print(f"✓ Training set class distribution:\n{y_train.value_counts()}")

# ===============================
# Step 4: Feature Scaling
# ===============================
print("\n[4/7] Feature Scaling (StandardScaler)...")
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)
print(f"✓ Scaler fitted on training data")
print(f"✓ Mean of scaled features: {X_train_scaled.mean():.6f}")
print(f"✓ Std of scaled features: {X_train_scaled.std():.6f}")

# ===============================
# Step 5: Handle Class Imbalance with SMOTE
# ===============================
print("\n[5/7] Handling Class Imbalance with SMOTE...")
smote = SMOTE(random_state=RANDOM_STATE)
X_train_smote, y_train_smote = smote.fit_resample(X_train_scaled, y_train)
print(f"✓ SMOTE applied")
print(f"✓ Training set after SMOTE: {X_train_smote.shape[0]} samples")
print(f"✓ Class distribution after SMOTE:\n{pd.Series(y_train_smote).value_counts()}")

# ===============================
# Step 6: Train Models
# ===============================
print("\n[6/7] Training Individual Models...")

# Logistic Regression
print("\n  > Training Logistic Regression...")
lr_model = LogisticRegression(max_iter=1000, random_state=RANDOM_STATE, solver='lbfgs')
lr_model.fit(X_train_smote, y_train_smote)
lr_pred = lr_model.predict(X_test_scaled)
lr_pred_proba = lr_model.predict_proba(X_test_scaled)[:, 1]
lr_accuracy = accuracy_score(y_test, lr_pred)
lr_f1 = f1_score(y_test, lr_pred)
lr_auc = roc_auc_score(y_test, lr_pred_proba)
print(f"    Accuracy: {lr_accuracy:.4f}, F1: {lr_f1:.4f}, AUC: {lr_auc:.4f}")

# Random Forest
print("\n  > Training Random Forest...")
rf_model = RandomForestClassifier(
    n_estimators=100, max_depth=15, random_state=RANDOM_STATE, n_jobs=-1
)
rf_model.fit(X_train_smote, y_train_smote)
rf_pred = rf_model.predict(X_test_scaled)
rf_pred_proba = rf_model.predict_proba(X_test_scaled)[:, 1]
rf_accuracy = accuracy_score(y_test, rf_pred)
rf_f1 = f1_score(y_test, rf_pred)
rf_auc = roc_auc_score(y_test, rf_pred_proba)
print(f"    Accuracy: {rf_accuracy:.4f}, F1: {rf_f1:.4f}, AUC: {rf_auc:.4f}")

# XGBoost
print("\n  > Training XGBoost...")
xgb_model = XGBClassifier(
    n_estimators=100, max_depth=7, learning_rate=0.1,
    random_state=RANDOM_STATE, use_label_encoder=False, eval_metric='logloss'
)
xgb_model.fit(X_train_smote, y_train_smote)
xgb_pred = xgb_model.predict(X_test_scaled)
xgb_pred_proba = xgb_model.predict_proba(X_test_scaled)[:, 1]
xgb_accuracy = accuracy_score(y_test, xgb_pred)
xgb_f1 = f1_score(y_test, xgb_pred)
xgb_auc = roc_auc_score(y_test, xgb_pred_proba)
print(f"    Accuracy: {xgb_accuracy:.4f}, F1: {xgb_f1:.4f}, AUC: {xgb_auc:.4f}")

# ===============================
# Step 7: Soft-Voting Ensemble
# ===============================
print("\n[7/7] Creating Soft-Voting Ensemble Model...")
ensemble_model = VotingClassifier(
    estimators=[
        ('logistic_regression', lr_model),
        ('random_forest', rf_model),
        ('xgboost', xgb_model)
    ],
    voting='soft'
)

# Fit the ensemble on the same training data
ensemble_model.fit(X_train_smote, y_train_smote)

# Ensemble predictions on test set
ensemble_pred = ensemble_model.predict(X_test_scaled)
ensemble_pred_proba = ensemble_model.predict_proba(X_test_scaled)[:, 1]
ensemble_accuracy = accuracy_score(y_test, ensemble_pred)
ensemble_precision = precision_score(y_test, ensemble_pred)
ensemble_recall = recall_score(y_test, ensemble_pred)
ensemble_f1 = f1_score(y_test, ensemble_pred)
ensemble_auc = roc_auc_score(y_test, ensemble_pred_proba)

print(f"✓ Ensemble Model Performance on Test Set:")
print(f"  - Accuracy:  {ensemble_accuracy:.4f}")
print(f"  - Precision: {ensemble_precision:.4f}")
print(f"  - Recall:    {ensemble_recall:.4f}")
print(f"  - F1 Score:  {ensemble_f1:.4f}")
print(f"  - AUC Score: {ensemble_auc:.4f}")

# Confusion Matrix
cm = confusion_matrix(y_test, ensemble_pred)
print(f"\nConfusion Matrix:\n{cm}")
print(f"True Negatives: {cm[0, 0]}, False Positives: {cm[0, 1]}")
print(f"False Negatives: {cm[1, 0]}, True Positives: {cm[1, 1]}")

# Classification Report
print(f"\nClassification Report:")
print(classification_report(y_test, ensemble_pred))

# ===============================
# Save Model and Scaler
# ===============================
print("\n" + "=" * 80)
print("SAVING MODEL AND SCALER")
print("=" * 80)

# Save ensemble model
joblib.dump(ensemble_model, MODEL_SAVE_PATH)
print(f"✓ Model saved to {MODEL_SAVE_PATH}")

# Save scaler
joblib.dump(scaler, SCALER_SAVE_PATH)
print(f"✓ Scaler saved to {SCALER_SAVE_PATH}")

# Save feature names for app.py
feature_info = {
    'feature_names': feature_names,
    'target_column': target_col
}
joblib.dump(feature_info, 'feature_info.pkl')
print(f"✓ Feature information saved to feature_info.pkl")

# ===============================
# Model Comparison Summary
# ===============================
print("\n" + "=" * 80)
print("MODEL PERFORMANCE COMPARISON")
print("=" * 80)

comparison_df = pd.DataFrame({
    'Model': ['Logistic Regression', 'Random Forest', 'XGBoost', 'Ensemble (Voting)'],
    'Accuracy': [lr_accuracy, rf_accuracy, xgb_accuracy, ensemble_accuracy],
    'F1 Score': [lr_f1, rf_f1, xgb_f1, ensemble_f1],
    'AUC Score': [lr_auc, rf_auc, xgb_auc, ensemble_auc]
})

print(comparison_df.to_string(index=False))

print("\n" + "=" * 80)
print("TRAINING COMPLETE!")
print("=" * 80)
print(f"\nReady for deployment. Use 'streamlit run app.py' to start the web application.")
print(f"Features: {len(feature_names)}")
print(f"Target: Binary Classification (0: No Heart Disease, 1: Heart Disease)")
