# 🔥 Deploy to Firebase (via Cloud Run)

Firebase Hosting doesn't directly support Python apps, but you can deploy using **Firebase + Cloud Run**.

## ⚠️ Important Note
For Streamlit apps, **Streamlit Cloud is easier and FREE**. 
Firebase deployment requires:
- Google Cloud account with billing enabled
- Docker knowledge
- More setup time

**Recommended:** Use Streamlit Cloud instead → See `DEPLOY_STREAMLIT_CLOUD.md`

---

## If You Still Want Firebase + Cloud Run:

### Prerequisites
1. Google Cloud account with billing enabled
2. Firebase CLI installed
3. Docker installed
4. gcloud CLI installed

### Step 1: Install Firebase CLI
```bash
npm install -g firebase-tools
```

### Step 2: Login to Firebase
```bash
firebase login
```

### Step 3: Initialize Firebase Project
```bash
firebase init hosting
```
- Select "Use an existing project" or create new
- Set public directory to "public"
- Configure as single-page app: No

### Step 4: Setup Google Cloud
```bash
# Login to gcloud
gcloud auth login

# Set project
gcloud config set project YOUR_PROJECT_ID

# Enable required APIs
gcloud services enable run.googleapis.com
gcloud services enable cloudbuild.googleapis.com
gcloud services enable artifactregistry.googleapis.com
```

### Step 5: Build and Push Docker Image
```bash
# Build the image
docker build -t gcr.io/YOUR_PROJECT_ID/pricewise-ai .

# Push to Container Registry
docker push gcr.io/YOUR_PROJECT_ID/pricewise-ai
```

### Step 6: Deploy to Cloud Run
```bash
gcloud run deploy pricewise-ai \
  --image gcr.io/YOUR_PROJECT_ID/pricewise-ai \
  --platform managed \
  --region us-central1 \
  --allow-unauthenticated \
  --memory 1Gi \
  --cpu 1 \
  --port 8080
```

### Step 7: Configure Firebase Hosting
Update `firebase.json`:
```json
{
  "hosting": {
    "public": "public",
    "rewrites": [
      {
        "source": "**",
        "run": {
          "serviceId": "pricewise-ai",
          "region": "us-central1"
        }
      }
    ]
  }
}
```

### Step 8: Deploy Firebase Hosting
```bash
firebase deploy --only hosting
```

### Step 9: Get Your URL
Your app will be available at:
```
https://YOUR_PROJECT_ID.web.app
```

---

## 💰 Cost Considerations
- Cloud Run: Pay per request (free tier available)
- Firebase Hosting: Free for basic usage
- Container Registry: Small storage costs

## 🎯 Easier Alternative: Streamlit Cloud

For hackathons, use **Streamlit Cloud** instead:
1. Go to https://share.streamlit.io
2. Sign in with GitHub
3. Select your repo
4. Click Deploy
5. Done! Free URL in 2 minutes!

See `DEPLOY_STREAMLIT_CLOUD.md` for details.

---

## Quick Commands Reference

```bash
# Firebase
firebase login
firebase init
firebase deploy

# Google Cloud
gcloud auth login
gcloud config set project PROJECT_ID
gcloud run deploy SERVICE_NAME --image IMAGE_URL

# Docker
docker build -t IMAGE_NAME .
docker push IMAGE_NAME
```

## 🆘 Troubleshooting

### "Permission denied"
- Enable billing on Google Cloud
- Enable required APIs

### "Container failed to start"
- Check Dockerfile CMD
- Verify port 8080 is exposed

### "Memory limit exceeded"
- Increase memory: `--memory 2Gi`

---

## 🏆 Recommendation for Hackathon

**Use Streamlit Cloud** - It's:
- ✅ Free
- ✅ Fast (2 min deploy)
- ✅ No billing required
- ✅ Auto-updates from GitHub
- ✅ Perfect for demos

Firebase + Cloud Run is better for production apps with custom domains and scaling needs.