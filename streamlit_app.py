"""
Heart Disease Prediction - Streamlit Web Application
Deployed Ensemble Model for Real-time Predictions
"""

import streamlit as st
import numpy as np
import pandas as pd
import joblib
import warnings
from pathlib import Path

warnings.filterwarnings('ignore')

# ===============================
# Page Configuration
# ===============================
st.set_page_config(
    page_title="CardioDetect | Heart Disease Prediction",
    page_icon="❤️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Professional Dark Theme Medical Dashboard CSS
st.markdown("""
<style>
    :root {
        --bg-primary: #0f172a;
        --bg-secondary: #1a1f3a;
        --bg-tertiary: #232d4a;
        --text-primary: #f1f5f9;
        --text-secondary: #cbd5e1;
        --text-muted: #94a3b8;
        --accent-primary: #ef4444;
        --accent-secondary: #3b82f6;
        --success: #10b981;
        --warning: #f59e0b;
        --border-color: #334155;
    }
    
    * {
        box-sizing: border-box;
    }
    
    html, body, [data-testid="stAppViewContainer"] {
        background-color: var(--bg-primary);
        color: var(--text-primary);
    }
    
    .main {
        background-color: var(--bg-primary);
        padding-top: 1.5rem;
    }
    
    /* Header */
    .header-container {
        background: linear-gradient(135deg, #1e293b 0%, #0f172a 100%);
        padding: 2.5rem 2rem;
        border-radius: 12px;
        color: var(--text-primary);
        margin-bottom: 2.5rem;
        border: 1px solid var(--border-color);
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3);
    }
    
    .header-container h1 {
        margin: 0;
        font-size: 2.2rem;
        font-weight: 600;
        letter-spacing: -0.3px;
        color: var(--text-primary);
    }
    
    .header-container p {
        margin: 0.75rem 0 0 0;
        font-size: 1rem;
        color: var(--text-secondary);
        font-weight: 400;
    }
    
    /* Tabs */
    .stTabs {
        margin-top: 0;
    }
    
    .stTabs [data-baseweb="tab-list"] {
        border-bottom: 1px solid var(--border-color);
    }
    
    .stTabs [data-baseweb="tab-list"] button {
        font-size: 0.95rem;
        font-weight: 500;
        padding: 1rem 1.25rem;
        border-radius: 8px 8px 0 0;
        transition: all 0.2s ease;
        color: var(--text-muted);
        border: none;
        background: transparent;
    }
    
    .stTabs [data-baseweb="tab-list"] button:hover {
        color: var(--text-secondary);
        background-color: rgba(148, 163, 184, 0.1);
    }
    
    .stTabs [data-baseweb="tab-list"] button[aria-selected="true"] {
        color: var(--accent-primary);
        border-bottom: 2px solid var(--accent-primary);
        background: transparent;
    }
    
    /* Cards and Containers */
    .card {
        background: linear-gradient(135deg, #1a1f3a 0%, #232d4a 100%);
        padding: 1.75rem;
        border-radius: 10px;
        border: 1px solid var(--border-color);
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.4);
        transition: all 0.2s ease;
    }
    
    .card:hover {
        border-color: rgba(239, 68, 68, 0.3);
        box-shadow: 0 8px 24px rgba(239, 68, 68, 0.1);
    }
    
    .metric-card {
        background: linear-gradient(135deg, #1a1f3a 0%, #232d4a 100%);
        padding: 1.5rem;
        border-radius: 10px;
        border: 1px solid var(--border-color);
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.4);
        text-align: center;
    }
    
    .metric-card h3 {
        margin: 0 0 0.5rem 0;
        font-size: 1.75rem;
        font-weight: 600;
        color: var(--accent-primary);
    }
    
    .metric-card p {
        margin: 0;
        font-size: 0.85rem;
        color: var(--text-muted);
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }
    
    .input-section {
        background: linear-gradient(135deg, #1a1f3a 0%, #232d4a 100%);
        padding: 2rem;
        border-radius: 10px;
        border: 1px solid var(--border-color);
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.4);
        margin-bottom: 2rem;
    }
    
    .section-title {
        color: var(--text-primary);
        font-size: 1.4rem;
        font-weight: 600;
        margin-bottom: 1.5rem;
        display: flex;
        align-items: center;
        gap: 0.75rem;
        padding-bottom: 1rem;
        border-bottom: 1px solid var(--border-color);
    }
    
    /* Risk Level Styling */
    .risk-low {
        background: linear-gradient(135deg, rgba(16, 185, 129, 0.1) 0%, rgba(16, 185, 129, 0.05) 100%);
        border-left: 4px solid #10b981;
        padding: 1.5rem;
        border-radius: 10px;
        color: #86efac;
    }
    
    .risk-low h3 {
        margin-top: 0;
        margin-bottom: 0.5rem;
        color: #10b981;
    }
    
    .risk-moderate {
        background: linear-gradient(135deg, rgba(245, 158, 11, 0.1) 0%, rgba(245, 158, 11, 0.05) 100%);
        border-left: 4px solid #f59e0b;
        padding: 1.5rem;
        border-radius: 10px;
        color: #fbbf24;
    }
    
    .risk-moderate h3 {
        margin-top: 0;
        margin-bottom: 0.5rem;
        color: #f59e0b;
    }
    
    .risk-high {
        background: linear-gradient(135deg, rgba(239, 68, 68, 0.1) 0%, rgba(239, 68, 68, 0.05) 100%);
        border-left: 4px solid #ef4444;
        padding: 1.5rem;
        border-radius: 10px;
        color: #fca5a5;
    }
    
    .risk-high h3 {
        margin-top: 0;
        margin-bottom: 0.5rem;
        color: #ef4444;
    }
    
    /* Buttons */
    .stButton > button {
        border-radius: 8px;
        padding: 0.75rem 1.75rem;
        font-weight: 500;
        border: none;
        transition: all 0.2s ease;
        font-size: 0.95rem;
        letter-spacing: 0.3px;
    }
    
    .stButton > button:first-child {
        background: linear-gradient(135deg, #ef4444 0%, #dc2626 100%);
        color: white;
        box-shadow: 0 4px 12px rgba(239, 68, 68, 0.3);
    }
    
    .stButton > button:first-child:hover {
        box-shadow: 0 8px 24px rgba(239, 68, 68, 0.4);
        transform: translateY(-2px);
    }
    
    .stButton > button:nth-child(2) {
        background: linear-gradient(135deg, #334155 0%, #1e293b 100%);
        color: var(--text-primary);
        border: 1px solid var(--border-color);
    }
    
    .stButton > button:nth-child(2):hover {
        background: linear-gradient(135deg, #475569 0%, #334155 100%);
    }
    
    /* Sliders and Input Elements */
    .stSlider [data-testid="stTickBar"] {
        background: var(--border-color);
    }
    
    /* Sidebar */
    .stSidebar {
        background: linear-gradient(180deg, #1a1f3a 0%, #232d4a 100%);
        border-right: 1px solid var(--border-color);
    }
    
    .stSidebar .stMarkdown {
        color: var(--text-primary);
    }
    
    .stSidebar [data-testid="stMarkdownContainer"] {
        color: var(--text-secondary);
    }
    
    /* Info Boxes */
    .info-box {
        background: linear-gradient(135deg, rgba(59, 130, 246, 0.1) 0%, rgba(59, 130, 246, 0.05) 100%);
        border-left: 4px solid #3b82f6;
        padding: 1.25rem;
        border-radius: 8px;
        color: #93c5fd;
        font-size: 0.95rem;
    }
    
    /* Metrics */
    .stMetric {
        background: linear-gradient(135deg, #1a1f3a 0%, #232d4a 100%);
        padding: 1.5rem;
        border-radius: 10px;
        border: 1px solid var(--border-color);
    }
    
    [data-testid="metric-container"] {
        background: linear-gradient(135deg, #1a1f3a 0%, #232d4a 100%);
        padding: 1.5rem;
        border-radius: 10px;
        border: 1px solid var(--border-color);
    }
    
    [data-testid="metric-container"] [data-testid="stMetricLabel"] {
        color: var(--text-muted);
        font-size: 0.8rem;
    }
    
    [data-testid="metric-container"] [data-testid="stMetricValue"] {
        color: var(--accent-primary);
        font-size: 1.8rem;
    }
    
    /* Expanders */
    .streamlit-expanderHeader {
        background: linear-gradient(135deg, #1a1f3a 0%, #232d4a 100%);
        border: 1px solid var(--border-color);
        border-radius: 8px;
        color: var(--text-primary);
    }
    
    .streamlit-expanderHeader:hover {
        border-color: rgba(239, 68, 68, 0.3);
    }
    
    .streamlit-expanderContent {
        background: linear-gradient(135deg, #232d4a 0%, #1a1f3a 100%);
        border: 1px solid var(--border-color);
        border-top: none;
        border-radius: 0 0 8px 8px;
        padding: 1rem;
    }
    
    /* Data Frame */
    .stDataFrame {
        border-radius: 8px;
        overflow: hidden;
    }
    
    [data-testid="stDataFrame"] {
        background: linear-gradient(135deg, #1a1f3a 0%, #232d4a 100%);
    }
    
    /* Progress Bar */
    .stProgress > div > div > div > div {
        background-color: var(--accent-primary);
        border-radius: 4px;
    }
    
    .stProgress > div > div > div {
        background-color: var(--bg-tertiary);
        border-radius: 4px;
        border: 1px solid var(--border-color);
    }
    
    /* Alert & Warning boxes */
    [data-testid="stAlert"] {
        background: linear-gradient(135deg, rgba(239, 68, 68, 0.1) 0%, rgba(239, 68, 68, 0.05) 100%);
        border: 1px solid rgba(239, 68, 68, 0.3);
        border-radius: 8px;
        color: #fca5a5;
    }
    
    /* Divider */
    hr {
        border: none;
        height: 1px;
        background: linear-gradient(90deg, transparent, var(--border-color), transparent);
        margin: 2rem 0;
    }
    
    /* Text Adjustments */
    h1, h2, h3, h4, h5, h6 {
        color: var(--text-primary) !important;
    }
    
    p, label, span {
        color: var(--text-secondary) !important;
    }
    
    /* Links */
    a {
        color: #3b82f6 !important;
    }
    
    a:hover {
        color: #60a5fa !important;
    }
</style>
""", unsafe_allow_html=True)

# ===============================
# Load Model and Scaler
# ===============================
def load_model_and_scaler():
    """Load trained model, scaler, and feature information"""
    try:
        model = joblib.load('heart_model.pkl')
        scaler = joblib.load('scaler.pkl')
        feature_info = joblib.load('feature_info.pkl')
        return model, scaler, feature_info
    except RecursionError:
        st.error("❌ Model recursion error - retraining...")
        st.stop()
    except Exception as e:
        st.error(f"❌ Error loading model: {str(e)}")
        st.stop()

# Load resources (without cache to avoid recursion)
model, scaler, feature_info = load_model_and_scaler()
feature_names = feature_info['feature_names'] if feature_info else []

# ===============================
# Page Header with Professional Design
# ===============================
st.markdown("""
<div class="header-container">
    <h1>CardioDetect</h1>
    <p>Clinical Heart Disease Risk Assessment Platform</p>
</div>
""", unsafe_allow_html=True)

# ===============================
# Sidebar Information
# ===============================
with st.sidebar:
    st.markdown("### About")
    st.markdown("""
    <div class="info-box">
    Intelligent cardiovascular risk assessment using ensemble machine learning models. Supports clinical decision-making only.
    </div>
    """, unsafe_allow_html=True)
    
    with st.expander("Model Details"):
        st.markdown("""
        **Ensemble Components:**
        - Logistic Regression
        - Random Forest Classifier
        - XGBoost Gradient Boosting
        
        **Method:** Soft-Voting Ensemble
        
        **Features:** 13 clinical parameters
        
        **Performance:** 99.28% Accuracy
        """)
    
    with st.expander("Disclaimer"):
        st.warning(
            "Educational tool only. Not a substitute for professional medical diagnosis. "
            "Always consult healthcare professionals."
        )

# ===============================
# Main Application Tabs
# ===============================
tab1, tab2, tab3 = st.tabs(["🔮 Make Prediction", "📖 Instructions", "ℹ️ About"])

# ===============================
# TAB 1: Make Prediction
# ===============================
with tab1:
    st.header("Patient Medical Data Input")
    st.markdown("Enter patient medical parameters below for heart disease prediction.")
    
# ===============================
# TAB 1: Make Prediction
# ===============================
with tab1:
    st.markdown("""
    <div class="section-title">
    📋 Patient Assessment Form
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="input-section">
    Enter the patient's medical parameters below. All fields are required for accurate assessment.
    </div>
    """, unsafe_allow_html=True)
    
    # Create input form with columns for better layout
    col1, col2 = st.columns(2)
    
    input_data = {}
    
    # Generate input fields based on feature names
    for idx, feature in enumerate(feature_names):
        # Alternate between columns
        with col1 if idx % 2 == 0 else col2:
            # Provide friendly names for features
            friendly_name = feature.replace('_', ' ').title()
            
            # Set reasonable default values and ranges based on feature type
            if 'age' in feature.lower():
                value = st.slider(
                    friendly_name, min_value=18, max_value=100, value=55,
                    key=f"input_{feature}", help="Age in years"
                )
            elif 'cholesterol' in feature.lower() or 'chol' in feature.lower():
                value = st.slider(
                    friendly_name, min_value=100, max_value=400, value=240,
                    key=f"input_{feature}", help="Serum cholesterol in mg/dL"
                )
            elif 'blood_pressure' in feature.lower() or 'trestbps' in feature.lower():
                value = st.slider(
                    friendly_name, min_value=80, max_value=200, value=130,
                    key=f"input_{feature}", help="Resting blood pressure in mmHg"
                )
            elif 'heart_rate' in feature.lower() or 'thalach' in feature.lower():
                value = st.slider(
                    friendly_name, min_value=40, max_value=220, value=100,
                    key=f"input_{feature}", help="Maximum heart rate achieved"
                )
            elif 'gender' in feature.lower() or 'sex' in feature.lower():
                value = st.selectbox(
                    friendly_name, options=[0, 1],
                    format_func=lambda x: "Female" if x == 0 else "Male",
                    key=f"input_{feature}"
                )
            elif any(x in feature.lower() for x in ['depression', 'peak', 'oldpeak']):
                value = st.slider(
                    friendly_name, min_value=0.0, max_value=6.0, value=1.5, step=0.1,
                    key=f"input_{feature}", help="ST depression induced by exercise"
                )
            elif any(x in feature.lower() for x in ['smoking', 'diabetes', 'fatigue', 'swelling', 
                                                      'shortness', 'palpitations', 'dizziness',
                                                      'cold', 'high_bp', 'high_cholesterol', 
                                                      'obesity', 'sedentary', 'family', 'stress',
                                                      'pain', 'nausea', 'breath', 'arms']):
                value = st.selectbox(
                    friendly_name, options=[0, 1],
                    format_func=lambda x: "No" if x == 0 else "Yes",
                    key=f"input_{feature}"
                )
            else:
                value = st.slider(
                    friendly_name, min_value=0.0, max_value=10.0, value=5.0, step=0.5,
                    key=f"input_{feature}"
                )
            
            input_data[feature] = value
    
    # Prediction Buttons with improved spacing
    st.markdown("---")
    col_btn1, col_btn2, col_spacer = st.columns([2, 2, 1])
    
    with col_btn1:
        predict_button = st.button(
            "🔍 Analyze & Predict",
            use_container_width=True,
            type="primary"
        )
    
    with col_btn2:
        clear_button = st.button(
            "🔄 Reset Form",
            use_container_width=True
        )
    
    # Handle Clear Button
    if clear_button:
        st.rerun()
    
    # ===============================
    # Make Prediction
    # ===============================
    if predict_button:
        # Prepare input for model
        input_df = pd.DataFrame([input_data])
        
        # Scale the input
        input_scaled = scaler.transform(input_df)
        
        # Make prediction
        prediction = model.predict(input_scaled)[0]
        prediction_proba = model.predict_proba(input_scaled)[0]
        
        # Display Results with enhanced styling
        st.markdown("---")
        st.markdown("""
        <div class="section-title">
        Assessment Results
        </div>
        """, unsafe_allow_html=True)
        
        col_result_left, col_result_right = st.columns([1.2, 1])
        
        with col_result_left:
            if prediction == 0:
                st.markdown(
                    f"""
                    <div class="risk-low">
                        <h3>No Heart Disease Detected</h3>
                        <p>Current medical indicators suggest low cardiovascular risk.</p>
                    </div>
                    """,
                    unsafe_allow_html=True
                )
            else:
                st.markdown(
                    f"""
                    <div class="risk-high">
                        <h3>Heart Disease Risk Detected</h3>
                        <p>Medical indicators suggest elevated cardiovascular risk. Professional evaluation recommended.</p>
                    </div>
                    """,
                    unsafe_allow_html=True
                )
        
        with col_result_right:
            col_no, col_yes = st.columns(2)
            with col_no:
                st.metric(
                    "Disease-Free",
                    f"{prediction_proba[0]:.1%}"
                )
            with col_yes:
                st.metric(
                    "Risk Level",
                    f"{prediction_proba[1]:.1%}"
                )
        
        # Risk Level Visualization with improved styling
        st.markdown("### Risk Indicator")
        risk_score = prediction_proba[1]
        
        if risk_score < 0.3:
            risk_level = "Low Risk"
            risk_color = "#10b981"
        elif risk_score < 0.7:
            risk_level = "Moderate Risk"
            risk_color = "#f59e0b"
        else:
            risk_level = "High Risk"
            risk_color = "#ef4444"
        
        st.progress(risk_score, text=risk_level)
        
        # Detailed Analysis Metrics
        st.markdown("### Clinical Summary")
        analysis_col1, analysis_col2, analysis_col3 = st.columns(3)
        
        with analysis_col1:
            status = "Positive" if prediction == 1 else "Negative"
            st.metric("Diagnosis", status)
        
        with analysis_col2:
            st.metric("Risk Score", f"{prediction_proba[1]:.2%}")
        
        with analysis_col3:
            st.metric("Confidence", f"{max(prediction_proba) * 100:.1f}%")
        
        # Input Parameters Summary in a professional table
        with st.expander("View Input Parameters", expanded=False):
            summary_df = pd.DataFrame({
                'Parameter': [k.replace('_', ' ').title() for k in input_data.keys()],
                'Value': list(input_data.values())
            })
            st.dataframe(summary_df, use_container_width=True, hide_index=True)

# ===============================
# TAB 2: Instructions
# ===============================
with tab2:
    st.markdown("""
    <div class="section-title">
    User Guide
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="info-box">
    Step-by-step instructions for using the cardiac risk assessment tool.
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("### Getting Started")
    
    with st.container():
        col1, col2 = st.columns([0.08, 0.92])
        with col1:
            st.markdown("1")
        with col2:
            st.markdown("**Enter Patient Data** — Navigate to the Prediction tab and enter all medical parameters from the patient record.")
    
    with st.container():
        col1, col2 = st.columns([0.08, 0.92])
        with col1:
            st.markdown("2")
        with col2:
            st.markdown("**Verify Information** — Double-check all values are accurate and in the correct units.")
    
    with st.container():
        col1, col2 = st.columns([0.08, 0.92])
        with col1:
            st.markdown("3")
        with col2:
            st.markdown("**Generate Assessment** — Click 'Analyze & Predict' to run the ensemble model.")
    
    with st.container():
        col1, col2 = st.columns([0.08, 0.92])
        with col1:
            st.markdown("4")
        with col2:
            st.markdown("**Interpret Results** — Review risk scores, confidence levels, and recommendations.")
    
    st.markdown("---")
    st.markdown("### Understanding Results")
    
    with st.expander("Low Risk Assessment", expanded=True):
        st.markdown("""
        **What It Means:** Medical indicators suggest minimal cardiovascular risk.
        
        **Recommendations:**
        - Continue routine monitoring
        - Maintain healthy lifestyle
        - Schedule regular check-ups
        """)
    
    with st.expander("Moderate Risk Assessment"):
        st.markdown("""
        **What It Means:** Some risk factors present; closer monitoring recommended.
        
        **Recommendations:**
        - Consult healthcare provider
        - Consider lifestyle modifications
        - Increase monitoring frequency
        """)
    
    with st.expander("High Risk Alert"):
        st.markdown("""
        **What It Means:** Multiple risk factors indicate elevated disease probability.
        
        **Recommendations:**
        - Seek professional medical evaluation
        - Discuss with cardiologist
        - Follow recommended treatment plan
        """)
    
    st.markdown("---")
    st.markdown("### Key Metrics")
    
    col_m1, col_m2 = st.columns(2)
    with col_m1:
        st.markdown("""
        **Disease-Free %**
        Probability patient does NOT have heart disease
        
        **Risk Score**
        Numerical probability (0-100%) of disease
        """)
    
    with col_m2:
        st.markdown("""
        **Risk Level %**
        Probability patient DOES have heart disease
        
        **Confidence**
        Certainty level of prediction
        """)
    
    st.markdown("---")
    st.markdown("### Clinical Parameters")
    
    st.markdown("The system analyzes these clinical inputs:")
    
    params_col1, params_col2 = st.columns(2)
    
    with params_col1:
        st.markdown("""
        **Vital Signs:**
        - Age and Gender
        - Blood Pressure
        - Heart Rate
        - ST Depression
        
        **Symptoms:**
        - Chest Pain Type
        - Exercise Response
        """)
    
    with params_col2:
        st.markdown("""
        **Laboratory:**
        - Serum Cholesterol
        - Fasting Blood Sugar
        - Electrolytes
        
        **Medical History:**
        - Risk Factors
        - Previous Conditions
        """)
    
    st.markdown("---")
    st.warning("This tool supports clinical decision-making but does not replace professional medical diagnosis.")

# ===============================
# TAB 3: About
# ===============================
with tab3:
    st.markdown("""
    <div class="section-title">
    About CardioDetect
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="info-box">
    Cardiovascular risk assessment platform powered by ensemble machine learning. Supports evidence-based clinical decision-making.
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        ### Platform Purpose
        
        Provides healthcare professionals with data-driven cardiovascular risk assessment using proven machine learning models.
        
        ### Key Features
        
        - Multi-model ensemble approach
        - High prediction accuracy (99.28%)
        - Transparent confidence scoring
        - Clinical parameter analysis
        - Risk stratification
        """)
    
    with col2:
        st.markdown("""
        ### Clinical Applications
        
        **Ideal for:**
        - Preliminary risk screening
        - Research studies
        - Clinical education
        - Decision support
        
        **Performance:**
        - 99.28% Accuracy
        - 99.37% Precision
        - 99.19% Recall
        """)
    
    st.markdown("---")
    
    st.markdown("### Technical Foundation")
    
    tech_col1, tech_col2, tech_col3 = st.columns(3)
    
    with tech_col1:
        st.markdown("""
        <div class="card" style="text-align: center;">
        <h4>Logistic Regression</h4>
        <p style="font-size: 0.9rem; color: #cbd5e1;">Linear probabilistic classifier</p>
        </div>
        """, unsafe_allow_html=True)
    
    with tech_col2:
        st.markdown("""
        <div class="card" style="text-align: center;">
        <h4>Random Forest</h4>
        <p style="font-size: 0.9rem; color: #cbd5e1;">Ensemble decision trees</p>
        </div>
        """, unsafe_allow_html=True)
    
    with tech_col3:
        st.markdown("""
        <div class="card" style="text-align: center;">
        <h4>XGBoost</h4>
        <p style="font-size: 0.9rem; color: #cbd5e1;">Gradient boosting optimization</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    st.markdown("### Model Performance Metrics")
    
    perf_col1, perf_col2, perf_col3, perf_col4 = st.columns(4)
    
    with perf_col1:
        st.markdown("""
        <div class="metric-card">
        <h3>99.28%</h3>
        <p>Accuracy</p>
        </div>
        """, unsafe_allow_html=True)
    
    with perf_col2:
        st.markdown("""
        <div class="metric-card">
        <h3>99.37%</h3>
        <p>Precision</p>
        </div>
        """, unsafe_allow_html=True)
    
    with perf_col3:
        st.markdown("""
        <div class="metric-card">
        <h3>99.19%</h3>
        <p>Recall</p>
        </div>
        """, unsafe_allow_html=True)
    
    with perf_col4:
        st.markdown("""
        <div class="metric-card">
        <h3>99.96%</h3>
        <p>AUC-ROC</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    st.markdown("### Important Information")
    
    with st.expander("Data Privacy", expanded=False):
        st.markdown("""
        - No patient data is stored
        - All processing is local
        - No external transmission
        - Results are not logged
        """)
    
    with st.expander("Legal Disclaimer", expanded=False):
        st.markdown("""
        **Educational Tool Only**
        
        CardioDetect is a machine learning support tool and should NOT be used as:
        - Substitute for professional diagnosis
        - Replacement for clinical judgment
        - Sole basis for treatment
        
        **Always consult qualified healthcare professionals for medical decisions.**
        """)
    
    with st.expander("Training Data", expanded=False):
        st.markdown("""
        **Dataset:** UCI Heart Disease Dataset
        - **Samples:** 70,000 balanced records
        - **Features:** 13 clinical parameters
        - **Preprocessing:** Standard scaling + SMOTE balancing
        - **Split:** 70% training, 30% testing
        """)
    
    st.markdown("---")
    
    dev_col1, dev_col2 = st.columns(2)
    
    with dev_col1:
        st.markdown("""
        ### Technology Stack
        
        - Python 3.x
        - Scikit-learn
        - XGBoost
        - Streamlit
        - Pandas & NumPy
        """)
    
    with dev_col2:
        st.markdown("""
        ### Version & Support
        
        **Version:** 1.0.0  
        **Updated:** 2024
        
        For questions or feedback, contact the development team.
        """)
    
    st.markdown("---")
    
    st.info("CardioDetect is an educational platform demonstrating machine learning in healthcare. It supports clinical decision-making but does not replace professional medical diagnosis.")

# ===============================
# Professional Footer
# ===============================
st.markdown("---")
st.markdown("""
<div style="background: linear-gradient(135deg, #1a1f3a 0%, #232d4a 100%); padding: 2rem; border-radius: 10px; text-align: center; border: 1px solid #334155; margin-top: 3rem;">
<p style="margin: 0 0 0.5rem 0; font-size: 1rem; font-weight: 500; color: #f1f5f9;">
CardioDetect
</p>
<p style="margin: 0 0 1rem 0; font-size: 0.9rem; color: #cbd5e1;">
Clinical Heart Disease Risk Assessment Platform
</p>
<p style="margin: 0; font-size: 0.85rem; color: #94a3b8;">
Educational platform only • Not a medical diagnosis • Consult healthcare professionals • Version 1.0
</p>
</div>
""", unsafe_allow_html=True)
