# 🌐 Online Deployment Guide - Solar Quote Engine

This guide will help you deploy the Solar Quote Engine to various online hosting platforms for production use.

## Prerequisites

- Git installed
- Python 3.8+ installed
- Basic understanding of Django
- Account on chosen hosting platform

## 🚀 Deployment Options

### Option 1: Heroku (Easiest for Beginners)

Heroku is a platform-as-a-service (PaaS) that makes deployment simple.

#### Step 1: Prepare Your Project

1. **Create a Django project** (if you haven't already):
```bash
django-admin startproject myproject
cd myproject
```

2. **Copy the solar_quote app** into your project:
```bash
# Copy the entire solar_quote folder into your project directory
```

3. **Update your project settings** (`myproject/settings.py`):
```python
INSTALLED_APPS = [
    # ... other apps
    'solar_quote',
]

# Add these at the bottom
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATIC_URL = '/static/'
```

4. **Update URLs** (`myproject/urls.py`):
```python
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('solar_quote.urls')),
]
```

#### Step 2: Install Heroku CLI

Download from: https://devcenter.heroku.com/articles/heroku-cli

#### Step 3: Create Heroku App

```bash
# Login to Heroku
heroku login

# Create app
heroku create your-solar-quote-app

# Add PostgreSQL database
heroku addons:create heroku-postgresql:mini
```

#### Step 4: Configure for Production

1. **Create `Procfile`** in project root:
```
web: gunicorn myproject.wsgi --log-file -
```

2. **Create `runtime.txt`**:
```
python-3.11.0
```

3. **Update `requirements.txt`**:
```bash
pip freeze > requirements.txt
```

Make sure it includes:
```
Django>=4.2
gunicorn>=21.2
psycopg2-binary>=2.9
whitenoise>=6.5
dj-database-url>=2.1
```

4. **Update `settings.py` for production**:
```python
import os
import dj_database_url

# Security
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'dev-key-change-in-production')
DEBUG = os.environ.get('DEBUG', 'False') == 'True'
ALLOWED_HOSTS = ['your-solar-quote-app.herokuapp.com', 'localhost']

# Database
DATABASES = {
    'default': dj_database_url.config(
        conn_max_age=600,
        conn_health_checks=True,
    )
}

# Static files with WhiteNoise
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # Add this
    # ... rest of middleware
]

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
```

#### Step 5: Deploy

```bash
# Initialize git (if not already)
git init
git add .
git commit -m "Initial commit"

# Deploy to Heroku
git push heroku main

# Run migrations
heroku run python manage.py migrate

# Create superuser
heroku run python manage.py createsuperuser

# Open your app
heroku open
```

#### Step 6: Set Environment Variables

```bash
heroku config:set DJANGO_SECRET_KEY='your-secret-key-here'
heroku config:set DEBUG=False
```

### Option 2: DigitalOcean App Platform

#### Step 1: Push to GitHub

1. Create a new repository on GitHub
2. Push your code:
```bash
git remote add origin https://github.com/yourusername/your-repo.git
git push -u origin main
```

#### Step 2: Create App on DigitalOcean

1. Go to https://cloud.digitalocean.com/apps
2. Click "Create App"
3. Connect your GitHub repository
4. Select your repository and branch

#### Step 3: Configure App

1. **Environment Variables**:
   - Add `DJANGO_SECRET_KEY`
   - Add `DEBUG=False`
   - Add `DATABASE_URL` (if using managed database)

2. **Build Command**:
```
pip install -r requirements.txt && python manage.py collectstatic --noinput && python manage.py migrate
```

3. **Run Command**:
```
gunicorn myproject.wsgi
```

4. Click "Create Resources"

### Option 3: PythonAnywhere

Great for beginners and has a free tier!

#### Step 1: Create Account

Go to https://www.pythonanywhere.com/ and create a free account

#### Step 2: Upload Your Code

1. Use the "Files" tab to upload your project, or
2. Use Git:
```bash
git clone https://github.com/yourusername/your-repo.git
```

#### Step 3: Create Virtual Environment

```bash
mkvirtualenv --python=/usr/bin/python3.10 myenv
pip install -r requirements.txt
```

#### Step 4: Configure Web App

1. Go to "Web" tab
2. Click "Add a new web app"
3. Choose "Manual configuration"
4. Select Python version
5. Configure:
   - Source code: `/home/yourusername/myproject`
   - Working directory: `/home/yourusername/myproject`
   - WSGI file: Edit to point to your project

#### Step 5: Edit WSGI File

```python
import os
import sys

path = '/home/yourusername/myproject'
if path not in sys.path:
    sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'myproject.settings'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
```

#### Step 6: Configure Static Files

In the Web tab, add:
- URL: `/static/`
- Directory: `/home/yourusername/myproject/staticfiles/`

Then run:
```bash
python manage.py collectstatic
```

### Option 4: Railway.app

Modern, simple platform with GitHub integration.

#### Step 1: Connect GitHub

1. Go to https://railway.app/
2. Sign up with GitHub
3. Click "New Project"
4. Select "Deploy from GitHub repo"

#### Step 2: Configure

Railway auto-detects Django projects. Add environment variables:
- `DJANGO_SECRET_KEY`
- `DEBUG=False`

#### Step 3: Add Database

Click "New" → "Database" → "PostgreSQL"

Railway automatically sets `DATABASE_URL`

### Option 5: AWS Elastic Beanstalk

For production-grade deployments with scalability.

#### Step 1: Install EB CLI

```bash
pip install awsebcli
```

#### Step 2: Initialize

```bash
eb init -p python-3.11 solar-quote-engine
```

#### Step 3: Create Environment

```bash
eb create solar-quote-env
```

#### Step 4: Configure

Create `.ebextensions/django.config`:
```yaml
option_settings:
  aws:elasticbeanstalk:container:python:
    WSGIPath: myproject.wsgi:application
  aws:elasticbeanstalk:application:environment:
    DJANGO_SETTINGS_MODULE: myproject.settings
```

#### Step 5: Deploy

```bash
eb deploy
eb open
```

## 🔒 Production Checklist

Before going live, ensure:

- [ ] `DEBUG = False` in production
- [ ] Strong `SECRET_KEY` set via environment variable
- [ ] `ALLOWED_HOSTS` configured correctly
- [ ] Database is PostgreSQL (not SQLite)
- [ ] Static files are collected and served
- [ ] HTTPS/SSL is enabled
- [ ] CSRF and security middleware enabled
- [ ] Environment variables for sensitive data
- [ ] Error logging configured
- [ ] Backups configured for database
- [ ] Monitoring set up

## 📊 Post-Deployment

After deployment:

1. **Test the application**:
   - Fill out the solar quote form
   - Verify calculations are correct
   - Test on mobile devices

2. **Access admin panel**:
   - Go to `your-domain.com/admin`
   - Login with superuser credentials
   - Verify you can see quotes

3. **Monitor**:
   - Check error logs
   - Monitor database usage
   - Watch for performance issues

## 🐛 Troubleshooting

### Static Files Not Loading

```python
# settings.py
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATIC_URL = '/static/'

# Run this
python manage.py collectstatic --noinput
```

### Database Connection Error

Make sure `DATABASE_URL` environment variable is set:
```bash
# Heroku
heroku config:set DATABASE_URL='your-database-url'
```

### 500 Server Error

Check logs:
```bash
# Heroku
heroku logs --tail

# DigitalOcean
Check runtime logs in dashboard

# PythonAnywhere
Check error log in Web tab
```

Enable detailed errors temporarily (remove after fixing):
```python
# settings.py
DEBUG = True  # Only for debugging!
```

## 🔐 Security Best Practices

1. **Never commit secrets**:
   - Use `.env` files (add to `.gitignore`)
   - Use environment variables
   - Use hosting platform's secret management

2. **Use strong SECRET_KEY**:
```python
# Generate a new one
from django.core.management.utils import get_random_secret_key
print(get_random_secret_key())
```

3. **Enable security features**:
```python
# settings.py for production
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_BROWSER_XSS_FILTER = True
X_FRAME_OPTIONS = 'DENY'
```

## 🎯 Custom Domain

Most platforms support custom domains:

1. **Purchase domain** (from Namecheap, GoDaddy, etc.)
2. **Add to hosting platform**:
   - Heroku: `heroku domains:add www.yourdomain.com`
   - Others: Check platform documentation
3. **Update DNS records** at your domain registrar:
   - Add CNAME record pointing to your app
   - Update ALLOWED_HOSTS in settings

## 💰 Cost Estimates

- **Heroku**: $7-25/month (Eco dyno + mini Postgres)
- **DigitalOcean**: $5-12/month (Basic app)
- **PythonAnywhere**: $5-12/month (Hacker plan)
- **Railway**: $5-20/month (Pay-as-you-go)
- **AWS**: $15-50/month (Variable based on traffic)

Free tiers available on:
- PythonAnywhere (limited)
- Railway (limited)
- Heroku Eco (limited hours)

## 📞 Support Resources

- Django Deployment: https://docs.djangoproject.com/en/stable/howto/deployment/
- Heroku Django Guide: https://devcenter.heroku.com/categories/django-support
- DigitalOcean Tutorials: https://www.digitalocean.com/community/tags/django
- Stack Overflow: Tag your questions with 'django' and 'deployment'

---

**Need help?** Check the detailed setup in `DJANGO_SETUP.md` or consult the Django documentation.

**Ready to deploy?** Choose a platform above and follow the step-by-step instructions! 🚀