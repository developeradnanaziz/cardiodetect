# CardioDetect - Complete Deployment Guide

## 🚀 Deployment Options Overview

Your Heart Disease Prediction app can be deployed using several methods. Choose the one that best fits your needs:

| Platform | Ease | Cost | Best For |
|----------|------|------|----------|
| **Streamlit Cloud** | ⭐⭐⭐⭐⭐ | FREE | Quick, easy deployment |
| **Hugging Face Spaces** | ⭐⭐⭐⭐⭐ | FREE | ML community |
| **Docker + AWS/Azure** | ⭐⭐⭐ | Varies | Production, scaling |
| **Heroku** | ⭐⭐⭐⭐ | $7+/month | Simple deployment |
| **PythonAnywhere** | ⭐⭐⭐⭐ | FREE/Paid | Simple hosting |
| **Local Server** | ⭐⭐⭐ | FREE | Internal use only |

---

## 🥇 Recommended: Streamlit Cloud (FREE & EASIEST)

### Why Streamlit Cloud?
- ✅ Built specifically for Streamlit apps
- ✅ Free tier available
- ✅ One-click deployment
- ✅ Automatic updates from GitHub
- ✅ HTTPS enabled
- ✅ No server management

### Step-by-Step Deployment

#### Step 1: Prepare Your Project on GitHub

1. **Create a GitHub account** (if you don't have one)
   - Go to: https://github.com
   - Sign up for free

2. **Create a new repository**
   - Click "New" repository
   - Name: `cardiodetect` (or your preferred name)
   - Make it PUBLIC
   - Click "Create repository"

3. **Clone the repository locally** (in PowerShell):
   ```powershell
   cd C:\
   git clone https://github.com/YOUR_USERNAME/cardiodetect.git
   cd cardiodetect
   ```

4. **Copy your project files**
   ```powershell
   Copy-Item "E:\Heart_Disease_Project\*" -Destination "C:\cardiodetect" -Recurse -Force
   ```

5. **Keep only essential files** (remove these):
   - `fresh_env/` (delete - virtual environment not needed)
   - `fresh_env_new/` (delete - virtual environment not needed)
   - `venv/` (delete - virtual environment not needed)
   - `__pycache__/` (delete - cache files)
   - `tempCodeRunnerFile.py` (delete - temporary file)
   - `run.bat`, `run.sh` (optional - not needed for cloud)

6. **Push to GitHub**:
   ```powershell
   cd C:\cardiodetect
   git add .
   git commit -m "Initial commit: CardioDetect heart disease prediction app"
   git push origin main
   ```

#### Step 2: Deploy on Streamlit Cloud

1. **Go to Streamlit Cloud**
   - Visit: https://streamlit.io/cloud
   - Click "Sign up"
   - Sign in with your GitHub account

2. **Deploy your app**
   - Click "New app"
   - Repository: Select your `cardiodetect` repository
   - Branch: `main`
   - Main file path: `streamlit_app.py`
   - Click "Deploy"

3. **Wait for deployment**
   - Takes 2-5 minutes
   - Your app URL: `https://cardiodetect-yourusername.streamlit.app`

#### Step 3: Share Your App
- Your app is now live!
- Share the URL with doctors, professors, or stakeholders
- URL example: `https://cardiodetect-yourusername.streamlit.app`

### Cost
**FREE** tier includes:
- Up to 3 app deployments
- Up to 1GB storage
- Community support

---

## 🤗 Alternative: Hugging Face Spaces (FREE & EASY)

### Why Hugging Face Spaces?
- ✅ Popular in ML community
- ✅ Completely free
- ✅ Simple GitHub integration
- ✅ Great for showcasing ML projects

### Deployment Steps

1. **Create Hugging Face account**
   - Go to: https://huggingface.co
   - Sign up

2. **Create a Space**
   - Click "New" → "New Space"
   - Name: `cardiodetect`
   - License: Choose one
   - Space SDK: **Streamlit**
   - Visibility: Public
   - Click "Create Space"

3. **Upload your files**
   - Via GitHub integration (recommended)
   - Or upload files directly

4. **Add required files**
   - `streamlit_app.py`
   - `requirements.txt`
   - `heart_model.pkl`
   - `scaler.pkl`
   - `feature_info.pkl`

5. **App deploys automatically**
   - URL: `https://huggingface.co/spaces/yourusername/cardiodetect`

### Cost
**COMPLETELY FREE** ✅

---

## 🐳 Docker Deployment (For Advanced Users)

### Create Docker Image

1. **Create `Dockerfile`** in your project root:

```dockerfile
FROM python:3.11-slim

WORKDIR /app

# Copy requirements
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy app files
COPY streamlit_app.py .
COPY heart_model.pkl .
COPY scaler.pkl .
COPY feature_info.pkl .

# Expose port
EXPOSE 8501

# Run Streamlit
CMD ["streamlit", "run", "streamlit_app.py", "--server.port=8501", "--server.address=0.0.0.0"]
```

2. **Build Docker image**:
   ```bash
   docker build -t cardiodetect:latest .
   ```

3. **Run Docker container locally**:
   ```bash
   docker run -p 8501:8501 cardiodetect:latest
   ```

4. **Deploy to cloud** (AWS/Azure/GCP/DigitalOcean):
   - Push image to container registry
   - Deploy from registry to cloud platform

---

## ☁️ AWS Deployment (Production-Grade)

### Using AWS App Runner (Easiest AWS Option)

1. **Create AWS account**
   - Go to: https://aws.amazon.com
   - Sign up for free tier

2. **Push Docker image to ECR**
   ```bash
   aws ecr create-repository --repository-name cardiodetect --region us-east-1
   docker tag cardiodetect:latest [YOUR_ECR_URI]/cardiodetect:latest
   docker push [YOUR_ECR_URI]/cardiodetect:latest
   ```

3. **Deploy with App Runner**
   - Open AWS Console
   - App Runner → Create service
   - Select ECR image
   - Configure and deploy
   - Get your public URL

### Cost
- **Free tier**: 12 months free for new customers
- **After**: ~$1-5/month depending on traffic

---

## 🌐 Local Server Deployment (Internal Networks)

### Run on Local Network

1. **Keep app running**:
   ```powershell
   E:\Heart_Disease_Project\fresh_env_new\Scripts\python.exe -m streamlit run streamlit_app.py --server.address=0.0.0.0
   ```

2. **Access from other computers on network**:
   - From same network: `http://YOUR_IP:8501`
   - From internet: Requires port forwarding (not recommended)

### Cost
**FREE** (requires your computer running 24/7)

---

## 📋 Pre-Deployment Checklist

### ✅ Files Required
- [x] `streamlit_app.py` - Main app file
- [x] `requirements.txt` - Dependencies
- [x] `heart_model.pkl` - Trained model
- [x] `scaler.pkl` - Feature scaler
- [x] `feature_info.pkl` - Feature metadata
- [x] `.gitignore` - For GitHub (see below)

### ✅ Create `.gitignore`
Create file `.gitignore` in project root:
```
# Virtual environments
venv/
fresh_env/
fresh_env_new/
env/

# Python
__pycache__/
*.pyc
*.pyo
*.egg-info/

# IDE
.vscode/
.idea/
*.swp

# OS
.DS_Store
.env

# Cache
*.cache
.streamlit/

# Temp files
tempCodeRunnerFile.py
*.tmp
```

### ✅ Update requirements.txt (Clean Version)
Your current `requirements.txt` is good:
```
numpy>=1.24.1,<2.0
pandas>=2.0.0
scikit-learn>=1.3.0
xgboost>=2.0.0
matplotlib>=3.8.0
seaborn>=0.12.0
imbalanced-learn>=0.11.0
streamlit>=1.28.0
```

### ✅ Create `.streamlit/config.toml`
Create folder `.streamlit` in project root, then create `config.toml`:
```toml
[theme]
primaryColor = "#ef4444"
backgroundColor = "#0f172a"
secondaryBackgroundColor = "#1a1f3a"
textColor = "#f1f5f9"
font = "sans serif"

[client]
showErrorDetails = false

[server]
maxUploadSize = 200
enableXsrfProtection = true
```

---

## 🎯 Quick Deployment Decision Tree

```
Do you want FREE deployment?
├─ YES → Go with Streamlit Cloud or Hugging Face Spaces
│   ├─ Do you have GitHub account?
│   │   ├─ YES → Streamlit Cloud (easiest)
│   │   └─ NO → Create GitHub account first
│   └─ Prefer ML community? → Hugging Face Spaces
└─ NO → Docker + AWS/Azure/GCP
    └─ Need help? → Use Heroku ($7+/month)
```

---

## 📊 Comparison Table

| Feature | Streamlit Cloud | Hugging Face | Docker | AWS | Heroku |
|---------|-----------------|--------------|--------|-----|--------|
| **Cost** | FREE | FREE | Free*  | $0-5/m | $7+/m |
| **Setup Time** | 5 min | 10 min | 30 min | 1 hour | 20 min |
| **Uptime** | 99% | 99% | Depends | 99.9% | 99.9% |
| **Scalability** | Good | Good | Excellent | Excellent | Good |
| **Custom Domain** | Premium | Free | Varies | Yes | Premium |
| **Best For** | Quick deploy | ML projects | Production | Enterprise | Quick cloud |

*Docker costs depend on cloud platform

---

## 🔐 Production Considerations

### Before Going Live

1. **Security**
   - ✅ No hardcoded credentials
   - ✅ Use environment variables for secrets
   - ✅ Enable HTTPS (done automatically on cloud)

2. **Performance**
   - ✅ Optimize model loading
   - ✅ Cache model in memory
   - ✅ Test with multiple simultaneous users

3. **Monitoring**
   - ✅ Set up error logging
   - ✅ Monitor uptime
   - ✅ Track usage metrics

4. **Compliance**
   - ✅ Add disclaimer: "For educational purposes"
   - ✅ Medical device regulations (varies by region)
   - ✅ Data privacy (GDPR, HIPAA if applicable)

### Add Disclaimer
Include in your app:
```python
st.warning(
    "⚠️ DISCLAIMER: This tool is for educational purposes only. "
    "It is NOT a substitute for professional medical diagnosis. "
    "Always consult qualified healthcare professionals."
)
```

---

## 🚀 QUICK START (Recommended)

### Deploy in 10 Minutes with Streamlit Cloud

1. **Create GitHub account** (2 min)
   - https://github.com/signup

2. **Create repository** (2 min)
   - New repo → Name: `cardiodetect` → Public

3. **Upload your files** (3 min)
   - Click "Add file" → "Upload files"
   - Select all project files

4. **Deploy on Streamlit Cloud** (3 min)
   - https://share.streamlit.io
   - Sign in with GitHub
   - Deploy

**Result**: Live app in 10 minutes! 🎉

---

## 📝 Post-Deployment

### After Successful Deployment

1. **Test your app**
   - Visit the deployed URL
   - Try making predictions
   - Test all features

2. **Share with others**
   - Share the URL
   - Works on any device with internet
   - No installation needed

3. **Get feedback**
   - From doctors/professors
   - From potential users
   - Iterate and improve

4. **Monitor performance**
   - Check logs
   - Track usage
   - Update when needed

---

## 🆘 Troubleshooting

### App won't start?
1. Check `requirements.txt` has all dependencies
2. Ensure model files are included
3. Check file paths are relative, not absolute

### Model not loading?
1. Verify pickle files exist
2. Check file naming matches code
3. Ensure compatible Python version

### Slow performance?
1. Optimize model loading with caching
2. Use `@st.cache_resource` decorator
3. Consider model quantization

### Out of memory?
1. Streamlit Cloud has memory limits
2. Optimize model size
3. Consider AWS/Azure for large models

---

## 📞 Support & Resources

### Official Documentation
- **Streamlit Cloud**: https://docs.streamlit.io/streamlit-cloud
- **Hugging Face Spaces**: https://huggingface.co/docs/hub/spaces
- **Docker**: https://docs.docker.com/
- **AWS**: https://aws.amazon.com/documentation/

### Community
- **Streamlit Forums**: https://discuss.streamlit.io
- **Hugging Face Discussions**: https://huggingface.co/spaces
- **Stack Overflow**: Tag `streamlit`

---

## ✅ Deployment Success Checklist

- [ ] GitHub account created
- [ ] Repository created and populated
- [ ] All required files included
- [ ] `requirements.txt` verified
- [ ] Model files (*.pkl) included
- [ ] `.streamlit/config.toml` created
- [ ] `.gitignore` created
- [ ] Code tested locally
- [ ] Pushed to GitHub
- [ ] Deployed to cloud platform
- [ ] App URL working
- [ ] Tested all features
- [ ] Shared with stakeholders

---

## 🎊 Congratulations!

Your CardioDetect application is ready for deployment!

**Recommended Path**: Streamlit Cloud (FREE, 10 minutes, no credit card needed)

**Next Step**: [Deploy on Streamlit Cloud](#-recommended-streamlit-cloud-free--easiest)

---

**Last Updated**: January 29, 2026
**Status**: Ready for Deployment ✅
