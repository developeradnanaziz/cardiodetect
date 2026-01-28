# Quick GitHub Setup for Deployment

## 🚀 Setup in 5 Steps

### Step 1: Create GitHub Account (Free)
```
1. Go to: https://github.com
2. Click "Sign up"
3. Enter email and password
4. Verify email
Done! ✅
```

### Step 2: Create New Repository
```
1. Click "+" icon (top right)
2. Select "New repository"
3. Repository name: cardiodetect
4. Description: Heart Disease Prediction App
5. Choose "Public"
6. Click "Create repository"
Done! ✅
```

### Step 3: Clone Repository to Your Computer

Open PowerShell and run:
```powershell
# Navigate to Documents folder
cd C:\Users\YourUsername\Documents

# Clone the repository
git clone https://github.com/YOUR_GITHUB_USERNAME/cardiodetect.git

# Enter the folder
cd cardiodetect
```

### Step 4: Copy Project Files

Copy all your project files:
```powershell
# Copy everything from your project
Copy-Item "E:\Heart_Disease_Project\*" -Destination "." -Recurse -Force

# Remove unnecessary folders (optional but recommended)
Remove-Item "fresh_env" -Recurse -Force
Remove-Item "fresh_env_new" -Recurse -Force
Remove-Item "venv" -Recurse -Force
Remove-Item "__pycache__" -Recurse -Force
Remove-Item "tempCodeRunnerFile.py" -Force
```

### Step 5: Push to GitHub

In PowerShell:
```powershell
# Check git is installed
git --version

# Configure git (do this once)
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"

# Add all files
git add .

# Create a commit
git commit -m "Initial commit: CardioDetect heart disease prediction app"

# Push to GitHub
git push -u origin main
```

**If you get an error about authentication:**
1. Go to: https://github.com/settings/tokens
2. Click "Generate new token"
3. Select scopes: `repo`, `workflow`
4. Copy the token
5. When Git asks for password, paste the token

---

## ✅ Files to Include

**Keep these:**
- ✅ `streamlit_app.py` - Main app
- ✅ `requirements.txt` - Dependencies
- ✅ `heart_model.pkl` - Model file
- ✅ `scaler.pkl` - Scaler file
- ✅ `feature_info.pkl` - Features file
- ✅ `README.md` - Project info
- ✅ `static/` - CSS and JS files
- ✅ `templates/` - HTML templates
- ✅ All documentation files

**Remove before uploading:**
- ❌ `fresh_env/` - Virtual environment
- ❌ `fresh_env_new/` - Virtual environment
- ❌ `venv/` - Virtual environment
- ❌ `__pycache__/` - Cache files
- ❌ `tempCodeRunnerFile.py` - Temp file
- ❌ `.git/` folders

---

## 📝 Create `.gitignore` File

Create a new file `.gitignore` in your project folder:

```
# Virtual environments
venv/
fresh_env/
fresh_env_new/
env/
__pycache__/

# Python
*.pyc
*.pyo
*.egg-info/
dist/
build/

# IDE
.vscode/
.idea/
*.swp
*.swo
*~

# OS
.DS_Store
Thumbs.db

# Environment
.env
.env.local

# Streamlit
.streamlit/cache/

# Temp
*.tmp
*.log
tempCodeRunnerFile.py
```

---

## 📁 Final Project Structure for GitHub

```
cardiodetect/
├── streamlit_app.py           ← Main app (REQUIRED)
├── requirements.txt           ← Dependencies (REQUIRED)
├── heart_model.pkl            ← Model (REQUIRED)
├── scaler.pkl                 ← Scaler (REQUIRED)
├── feature_info.pkl           ← Features (REQUIRED)
├── .gitignore                 ← Tell git what to ignore
├── .streamlit/
│   └── config.toml            ← Streamlit config
├── README.md                  ← Project info
├── static/
│   ├── css/
│   └── js/
├── templates/
│   └── *.html
└── [documentation files]
```

---

## ✅ Verify Everything is Uploaded

Check GitHub:
```
1. Go to: https://github.com/YOUR_USERNAME/cardiodetect
2. Should see:
   - streamlit_app.py
   - requirements.txt
   - All .pkl files
   - README.md
   - Other files
```

---

## 🎯 Next Step: Deploy on Streamlit Cloud

Once your files are on GitHub:

1. Go to: https://share.streamlit.io
2. Sign in with GitHub
3. Click "New app"
4. Select:
   - Repository: `cardiodetect`
   - Branch: `main`
   - Main file: `streamlit_app.py`
5. Click "Deploy"
6. Wait 2-5 minutes
7. Your app is LIVE! 🎉

---

## 🆘 Common Issues

### Git command not found?
```powershell
# Install git
# Download from: https://git-scm.com/download/win
# Or use: choco install git
```

### "Please tell me who you are"?
```powershell
git config --global user.name "Your Name"
git config --global user.email "your@email.com"
```

### "fatal: The current branch main does not have any upstream"?
```powershell
git push -u origin main
```

### Changes not showing on GitHub?
```powershell
git status                    # Check what changed
git add .                     # Add all changes
git commit -m "Update app"    # Commit
git push                      # Push to GitHub
```

---

## 📊 GitHub & Streamlit Cloud Free

✅ **GitHub**: 100% FREE
✅ **Streamlit Cloud**: FREE tier includes:
   - 3 app deployments
   - 1GB storage per app
   - Unlimited users
   - HTTPS encryption

**Total cost: $0** 💰

---

**Ready to deploy? Follow these 5 steps and your app will be live in 10 minutes!** 🚀
