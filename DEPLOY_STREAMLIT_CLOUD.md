# 🚀 Deploy to Streamlit Cloud (FREE & EASY)

## Why Streamlit Cloud?
- ✅ **100% Free** for public apps
- ✅ **One-click deploy** from GitHub
- ✅ **Auto-updates** when you push code
- ✅ **Custom URL** (yourapp.streamlit.app)
- ✅ **Perfect for hackathons**

## 📋 Step-by-Step Deployment

### Step 1: Go to Streamlit Cloud
Open: **https://share.streamlit.io**

### Step 2: Sign In with GitHub
- Click "Sign in with GitHub"
- Authorize Streamlit to access your repositories

### Step 3: Deploy Your App
1. Click **"New app"** button
2. Select your repository: `nesaguru2005-rgb/AI-Driven-Hotel-Flight-Price-Forecasting-System`
3. Branch: `main`
4. Main file path: `app.py`
5. Click **"Deploy!"**

### Step 4: Wait for Deployment
- Streamlit will install dependencies from `requirements.txt`
- Build takes 2-5 minutes
- You'll get a live URL when done!

## 🌐 Your Live URL
After deployment, your app will be available at:
```
https://[your-app-name].streamlit.app
```

Example:
```
https://ai-price-forecaster.streamlit.app
```

## 📱 Share Your App
Once deployed, share the URL with:
- Hackathon judges
- Team members
- Anyone in the world!

## 🔄 Auto-Updates
Every time you push to GitHub, Streamlit Cloud automatically redeploys!

```bash
git add .
git commit -m "Update feature"
git push
# App auto-updates in ~1 minute!
```

## ⚙️ Advanced Settings (Optional)

### Custom Domain
1. Go to app settings
2. Add custom domain
3. Configure DNS

### Secrets Management
For API keys (if needed):
1. Go to app settings
2. Click "Secrets"
3. Add in TOML format

## 🎯 Quick Deploy Checklist

- [x] Code pushed to GitHub ✅
- [x] requirements.txt present ✅
- [x] app.py as main file ✅
- [x] .streamlit/config.toml configured ✅
- [x] data/ folder with CSV files ✅
- [x] models/ folder with .pkl files ✅
- [ ] Sign in to share.streamlit.io
- [ ] Click "New app"
- [ ] Select repository and deploy
- [ ] Get your live URL!

## 🏆 Perfect for Hackathon!

Benefits for your presentation:
- **Live demo** - No local setup needed
- **Shareable URL** - Judges can try it themselves
- **Professional** - Shows deployment skills
- **Reliable** - Won't crash during demo

## 🆘 Troubleshooting

### "Module not found" error
- Check requirements.txt has all packages
- Redeploy the app

### "File not found" error
- Ensure data/ and models/ folders are committed
- Check file paths in code

### App crashes
- Check Streamlit Cloud logs
- Look for Python errors

## 🎉 You're Ready!

Your app is already configured for Streamlit Cloud deployment.
Just follow the steps above and you'll have a live URL in minutes!

**Deploy now:** https://share.streamlit.io