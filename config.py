# CardioPredict Configuration

## Application Settings
FLASK_ENV=development
FLASK_DEBUG=True
SECRET_KEY=your-secret-key-here

## Server Settings
HOST=0.0.0.0
PORT=5000

## Model Settings
MODEL_PATH=heart_model.pkl
SCALER_PATH=scaler.pkl

## SHAP Settings
SHAP_BACKGROUND_SIZE=100
SHAP_PLOT_DPI=100

## Feature Validation
MIN_AGE=18
MAX_AGE=100

MIN_BP=80
MAX_BP=200

MIN_CHOLESTEROL=100
MAX_CHOLESTEROL=400

MIN_HEART_RATE=40
MAX_HEART_RATE=220

## Medical Parameters
RISK_THRESHOLDS={"low": 0.3, "moderate": 0.6, "high": 0.8}

## Logging
LOG_LEVEL=INFO
LOG_FILE=cardiopredict.log

## Security
CORS_ORIGINS=["http://localhost:5000", "http://127.0.0.1:5000"]
RATE_LIMIT=100/hour

## Database (optional for future use)
DATABASE_URL=sqlite:///cardiopredict.db
