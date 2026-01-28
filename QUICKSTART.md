# CardioPredict - Quick Reference Guide

## 📋 What's Included

### Core Files
- ✅ **app.py** - Flask backend with all routes and SHAP integration
- ✅ **heart_model.py** - ML model training script
- ✅ **heart_model.pkl** - Trained ensemble model
- ✅ **scaler.pkl** - Feature scaling object
- ✅ **heart.csv** - Training dataset (70,000 patient records)

### Web Interface
- ✅ **templates/base.html** - Header, navigation, footer
- ✅ **templates/index.html** - Complete dashboard (form + results)
- ✅ **static/css/style.css** - Professional dark theme (1000+ lines)
- ✅ **static/js/main.js** - Core functionality & API calls
- ✅ **static/js/form.js** - Form validation & error handling
- ✅ **static/js/visualization.js** - Charts & visualization

### Configuration & Docs
- ✅ **requirements.txt** - All dependencies
- ✅ **config.py** - Configuration template
- ✅ **README.md** - Full documentation
- ✅ **DEPLOYMENT.md** - Production setup guide
- ✅ **TECHNICAL_SPECS.md** - Architecture & features
- ✅ **test_api.py** - API test suite
- ✅ **run.bat** - Windows startup
- ✅ **run.sh** - macOS/Linux startup

---

## 🚀 Getting Started (30 seconds)

### Windows
```bash
run.bat
```

### macOS/Linux
```bash
chmod +x run.sh
./run.sh
```

Then open: **http://localhost:5000**

---

## 🎯 Key Features at a Glance

| Feature | Status | Details |
|---------|--------|---------|
| **18-Feature Form** | ✅ | All medical fields with validation |
| **Ensemble Model** | ✅ | 99.28% accuracy (3 models voting) |
| **SHAP Analysis** | ✅ | Auto-generated per patient |
| **Dark Theme UI** | ✅ | Professional hospital design |
| **Responsive Design** | ✅ | Desktop, tablet, mobile |
| **Form Validation** | ✅ | Real-time client + server-side |
| **Results Visualization** | ✅ | Risk meter, probability charts |
| **Report Download** | ✅ | Export as text file |
| **API Endpoints** | ✅ | POST /api/predict + others |
| **Error Handling** | ✅ | Graceful with user feedback |

---

## 📊 Model Performance

```
Logistic Regression:  99.19%
Random Forest:        99.19%
XGBoost:              99.27%
━━━━━━━━━━━━━━━━━━━
Ensemble (Best):      99.28% ⭐
```

---

## 🏥 Medical Features

**18 Total Features organized by category:**

```
Demographics         Cardiovascular       Laboratory         ECG & Advanced
├─ Age              ├─ Resting BP        ├─ Cholesterol      ├─ ECG Results
└─ Sex              ├─ Max Heart Rate    ├─ Total Chol        ├─ ST Depression
                    ├─ Diastolic BP      └─ Blood Sugar       ├─ ST Slope
Symptoms            └─ Resting HR                            
├─ Chest Pain Type  (4 values)           Cardiac Imaging
└─ Exercise Angina  (Yes/No)             ├─ Major Vessels
                                         ├─ Thalassemia Type
                                         └─ Chest Pain Level
```

---

## 💻 System Requirements

- **Python**: 3.8+
- **RAM**: 2GB minimum
- **Disk**: 500MB (with models)
- **Browser**: Modern (Chrome, Firefox, Safari, Edge)

---

## 🔗 API Quick Reference

### GET /
Dashboard page

### POST /api/predict
**Body**: 18 patient features (JSON)
**Response**: Prediction + SHAP plot

### GET /api/feature-info
Feature metadata and validation rules

### GET /health
Server status check

---

## 📁 File Locations

```
Home Page:          http://localhost:5000/
API Prediction:     POST http://localhost:5000/api/predict
Feature Info:       http://localhost:5000/api/feature-info
Health Check:       http://localhost:5000/health
```

---

## 🧪 Testing

```bash
# Test all endpoints
python test_api.py
```

Tests:
- ✅ Health endpoint
- ✅ Feature information
- ✅ Low-risk prediction
- ✅ Moderate-risk prediction
- ✅ High-risk prediction

---

## 🔧 Configuration

Edit `config.py` for:
- Port number (default: 5000)
- Debug mode (default: On for development)
- Model/scaler paths
- Validation thresholds

---

## 📝 Common Tasks

### Change Port
Edit `app.py` line ~230:
```python
app.run(debug=True, host='0.0.0.0', port=8000)
```

### Retrain Models
```bash
python heart_model.py
```

### Disable Debug Mode
Edit `app.py` line ~230:
```python
app.run(debug=False)  # Production mode
```

### Check Dependencies
```bash
pip list
```

---

## 🐛 Troubleshooting

| Issue | Solution |
|-------|----------|
| Port 5000 in use | Change port in app.py or kill process |
| Models not found | Run `python heart_model.py` |
| Dependencies missing | Run `pip install -r requirements.txt` |
| SHAP slow | Normal - 1-2 seconds for visualization |
| CSS not loading | Check static/css/style.css exists |
| Form not working | Check browser console (F12) |

---

## 📚 Documentation

- **README.md** - Complete user guide
- **DEPLOYMENT.md** - Production setup (Docker, Nginx, SSL)
- **TECHNICAL_SPECS.md** - Architecture details
- **Code comments** - Extensive inline documentation

---

## 🎓 Understanding the Code

### Form Submission
```javascript
// static/js/main.js
handleFormSubmit() → Gather data → Send to /api/predict
```

### Prediction Process
```python
# app.py
Receive features → Scale → Ensemble prediction → SHAP analysis → Return JSON
```

### Results Display
```javascript
// static/js/main.js
displayResults() → Animate values → Show SHAP plot → Enable actions
```

---

## 🔐 Security Notes

- Server validates all inputs
- No sensitive data in URLs
- HTTPS ready for production
- Models loaded at startup (cache)
- CORS can be restricted per deployment

---

## ⚠️ Important Reminder

**This system is for medical professionals only.**
- Not for self-diagnosis
- Always consult qualified cardiologists
- Use AI as assistive tool only
- Clinical judgment is essential

---

## 💡 Tips

1. **First run slow?** - Model loading takes ~2-3 seconds
2. **SHAP plot slow?** - Normal for first prediction (cached after)
3. **Test data?** - Use test_api.py for sample patients
4. **Production ready?** - See DEPLOYMENT.md for Gunicorn/Docker setup
5. **Mobile test?** - Responsive design adapts automatically

---

## 📞 Files Summary

| File | Purpose | Size |
|------|---------|------|
| app.py | Flask backend | ~230 lines |
| heart_model.py | ML training | ~146 lines |
| index.html | Dashboard | ~400 lines |
| style.css | Styling | ~1000+ lines |
| main.js | Functionality | ~350 lines |
| form.js | Validation | ~300 lines |
| visualization.js | Charts | ~250 lines |

---

## 🎯 Next Steps

1. ✅ Start the server (`run.bat` or `run.sh`)
2. ✅ Open http://localhost:5000
3. ✅ Fill form with patient data
4. ✅ Click "Analyze Patient"
5. ✅ Review results and SHAP plot
6. ✅ Download report if needed

---

**CardioPredict v1.0** | Professional Heart Disease Risk Assessment
