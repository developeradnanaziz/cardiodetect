# CardioPredict - Professional Heart Disease Risk Assessment System

## Overview

CardioPredict is a sophisticated medical AI system that predicts heart disease risk using an ensemble of machine learning models with explainable AI (SHAP). Built with Python, Flask, and modern web technologies, it provides a professional dashboard for medical professionals.

### Key Features

✅ **Advanced ML Ensemble**
- Logistic Regression
- Random Forest Classifier
- XGBoost Classifier
- Soft Voting Ensemble (99.28% accuracy)

✅ **Professional Dashboard**
- Dark theme optimized for medical professionals
- 18-feature patient data form
- Real-time prediction with risk visualization
- SHAP feature importance analysis

✅ **Explainability**
- SHAP (SHapley Additive exPlanations) values
- Feature importance visualization
- Doctor-friendly interpretation

✅ **Responsive Design**
- Desktop and mobile optimized
- Smooth animations and transitions
- Professional medical UI

## Installation

### Prerequisites
- Python 3.8+
- pip or conda package manager

### Setup

1. **Navigate to project directory:**
```bash
cd Heart_Disease_Project
```

2. **Create virtual environment (recommended):**
```bash
python -m venv venv
source venv/Scripts/activate  # On Windows
# or
source venv/bin/activate  # On macOS/Linux
```

3. **Install dependencies:**
```bash
pip install -r requirements.txt
```

Or install individually:
```bash
pip install flask numpy pandas scikit-learn xgboost shap matplotlib seaborn
```

4. **Train models (if not already done):**
```bash
python heart_model.py
```

This will generate:
- `heart_model.pkl` - Trained ensemble model
- `scaler.pkl` - Feature scaler

## Running the Application

### Start the Flask Server

```bash
python app.py
```

The application will be available at:
- Local: `http://localhost:5000/`
- Network: `http://<your-ip>:5000/`

### Using the Dashboard

1. **Enter Patient Information:**
   - Fill in all 18 medical features in the form
   - Fields include demographics, vitals, lab values, and imaging

2. **Analyze Patient:**
   - Click "Analyze Patient" button
   - System processes data and generates prediction

3. **Review Results:**
   - Risk percentage (0-100%)
   - Disease/Healthy probability
   - Confidence level
   - SHAP feature importance plot

4. **Download Report:**
   - Click "Download Report" to export results as text file

## Project Structure

```
Heart_Disease_Project/
├── app.py                    # Flask backend
├── heart_model.py            # Model training
├── heart.csv                 # Training data
├── heart_model.pkl           # Saved ensemble model
├── scaler.pkl               # Feature scaler
├── templates/
│   ├── base.html            # Base template
│   └── index.html           # Main dashboard
├── static/
│   ├── css/
│   │   └── style.css        # Dark theme styling
│   └── js/
│       ├── main.js          # Core functionality
│       ├── form.js          # Form validation
│       └── visualization.js # Charts & analytics
└── README.md
```

## Medical Features (18 Total)

### Demographics
- **Age** (years): 18-100
- **Sex** (M/F)

### Symptoms & Clinical History
- **Chest Pain Type**: Typical Angina, Atypical, Non-anginal, Asymptomatic
- **Exercise Induced Angina**: Yes/No

### Cardiovascular Metrics
- **Resting Blood Pressure** (mmHg): 80-200
- **Max Heart Rate Achieved** (bpm): 60-220
- **Diastolic Blood Pressure** (mmHg): 40-130
- **Resting Heart Rate** (bpm): 40-200

### Laboratory Values
- **Serum Cholesterol** (mg/dl): 100-400
- **Total Cholesterol** (mg/dl): 100-400
- **Fasting Blood Sugar > 120**: Yes/No

### Electrocardiogram & Advanced Metrics
- **Resting ECG Results**: Normal, ST-T Abnormality, LV Hypertrophy
- **ST Depression (Exercise)** (mm): 0-6
- **ST Segment Depression** (mm): 0-10
- **ST Segment Slope**: Upsloping, Flat, Downsloping

### Cardiac Imaging & Risk Factors
- **Major Vessels (Fluoroscopy)**: 0-3 vessels
- **Thalassemia Type**: Normal, Fixed Defect, Reversible Defect
- **Chest Pain Severity**: 0-3

## API Endpoints

### GET /
Returns the main dashboard HTML page.

### POST /api/predict
**Request Body:**
```json
{
  "age": 55,
  "sex": 1,
  "cp": 0,
  "trestbps": 130,
  "chol": 240,
  "fbs": 0,
  "restecg": 1,
  "thalach": 150,
  "exang": 0,
  "oldpeak": 1.5,
  "slope": 1,
  "ca": 1,
  "thal": 2,
  "chest_pain_type": 1,
  "blood_pressure": 85,
  "cholesterol": 250,
  "heart_rate": 75,
  "st_depression": 0.5
}
```

**Response:**
```json
{
  "success": true,
  "prediction": 0,
  "diagnosis": "No Heart Disease",
  "risk_percentage": 15.25,
  "confidence": 98.5,
  "diagnosis_color": "success",
  "shap_plot": "data:image/png;base64,...",
  "probabilities": {
    "healthy": 84.75,
    "diseased": 15.25
  }
}
```

### GET /api/feature-info
Returns metadata about form fields and validation rules.

### GET /health
Health check endpoint.
```json
{
  "status": "healthy",
  "model_loaded": true,
  "scaler_loaded": true
}
```

## Model Performance

| Model | Accuracy |
|-------|----------|
| Logistic Regression | 99.19% |
| Random Forest | 99.19% |
| XGBoost | 99.27% |
| **Ensemble (Voting)** | **99.28%** |

## Technical Stack

**Backend:**
- Flask 3.0+ - Web framework
- scikit-learn - ML algorithms
- XGBoost - Gradient boosting
- SHAP - Explainability
- Matplotlib - Visualization

**Frontend:**
- HTML5 - Structure
- CSS3 - Dark theme styling
- JavaScript (ES6+) - Interactivity
- Responsive design - Mobile & desktop

**Deployment Ready:**
- Supports production WSGI servers (Gunicorn, uWSGI)
- Can be containerized with Docker
- Scalable architecture

## Usage Example

### From Browser
1. Navigate to `http://localhost:5000`
2. Fill patient form with medical data
3. Click "Analyze Patient"
4. View results with SHAP visualization
5. Download report if needed

### From Python Script
```python
import requests
import json

patient_data = {
    "age": 55,
    "sex": 1,
    "cp": 0,
    # ... other features
}

response = requests.post(
    'http://localhost:5000/api/predict',
    json=patient_data
)

result = response.json()
print(f"Risk: {result['risk_percentage']}%")
print(f"Diagnosis: {result['diagnosis']}")
```

## Important Disclaimers

⚠️ **Medical Use Disclaimer:**
- This system is designed as an **assistive tool for medical professionals only**
- **Not for self-diagnosis** or public health applications
- Must be used under supervision of qualified healthcare providers
- AI predictions should be combined with clinical judgment
- Always consult qualified cardiologists for final diagnosis
- No AI system should replace human medical expertise

## Development & Troubleshooting

### Common Issues

**Models not loading:**
```
Error: No such file or directory: 'heart_model.pkl'
```
Solution: Run `python heart_model.py` to train models first.

**Port already in use:**
Change port in `app.py`:
```python
app.run(debug=True, host='0.0.0.0', port=5001)
```

**SHAP plot generation slow:**
The system uses XGBoost TreeExplainer which is computationally efficient. First prediction may take 2-3 seconds.

### Logging
Flask debug mode is enabled by default. Check console for detailed logs:
```
 * Running on http://localhost:5000
 * Debugger PIN: 123-456-789
```

## Performance Optimization

- **Frontend:** CSS Grid, lazy loading, minimal JavaScript
- **Backend:** Model caching, vectorized operations
- **SHAP:** Background computation, result caching
- **Database Ready:** Can integrate with PostgreSQL/MongoDB

## Future Enhancements

- [ ] Multi-language support (English, Spanish, French)
- [ ] Patient data persistence with database
- [ ] Historical trend analysis
- [ ] PDF report generation
- [ ] Integration with EHR systems
- [ ] Mobile app (React Native)
- [ ] Real-time dashboard analytics
- [ ] Model versioning and A/B testing

## License & Citation

CardioPredict © 2026
Professional AI System for Medical Assessment

**Citation:**
```
CardioPredict: Heart Disease Risk Assessment System
Using Ensemble Machine Learning with SHAP Explainability
```

## Support & Documentation

For questions, issues, or feature requests:
1. Check the API documentation in `/api/feature-info`
2. Review Flask debug output
3. Check browser console (F12) for client-side errors

---

**Built with ❤️ for medical professionals**

*CardioPredict v1.0 | Powered by Advanced Machine Learning & Explainable AI*
