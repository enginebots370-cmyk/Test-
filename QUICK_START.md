# 🚀 Quick Start Guide - Solar Quote Engine

This guide will help you get the Solar Quote Engine running in the fastest way possible.

## 🎯 Three Ways to Start

### Option 1: Instant Test (0 Setup Required) ⚡
**Best for:** Quick demo, testing, or if you don't have Python/Django installed

**Steps:**
1. Open the `index.html` file in any web browser
   ```bash
   # On Mac
   open index.html
   
   # On Linux
   xdg-open index.html
   
   # On Windows
   start index.html
   
   # Or just double-click the file!
   ```

2. Fill out the form and click "Calculate My Solar Quote"

3. View your instant solar quote with:
   - System size recommendation
   - Cost estimates with tax credits
   - Savings calculations
   - Environmental impact

**That's it!** No server, no installation, works immediately.

---

### Option 2: Local Django Server (Recommended) 🐍
**Best for:** Development, customization, or deploying later

**Prerequisites:**
- Python 3.8+ installed
- pip (Python package manager)

**Steps:**

1. **Install Django** (if not already installed):
   ```bash
   pip install Django>=4.2
   ```

2. **Navigate to the project directory**:
   ```bash
   cd /path/to/Test-
   ```

3. **Create a simple Django project** (if you don't have one):
   ```bash
   django-admin startproject myproject .
   ```

4. **Add solar_quote to INSTALLED_APPS**:
   
   Edit `myproject/settings.py` and add:
   ```python
   INSTALLED_APPS = [
       'django.contrib.admin',
       'django.contrib.auth',
       'django.contrib.contenttypes',
       'django.contrib.sessions',
       'django.contrib.messages',
       'django.contrib.staticfiles',
       'solar_quote',  # Add this line
   ]
   
   # Add at the bottom:
   STATIC_URL = '/static/'
   STATIC_ROOT = BASE_DIR / 'staticfiles'
   ```

5. **Configure URLs**:
   
   Edit `myproject/urls.py`:
   ```python
   from django.contrib import admin
   from django.urls import path, include
   
   urlpatterns = [
       path('admin/', admin.site.urls),
       path('', include('solar_quote.urls')),
   ]
   ```

6. **Run the automated setup**:
   ```bash
   cd solar_quote
   ./setup.sh
   ```
   
   Or manually:
   ```bash
   python manage.py makemigrations solar_quote
   python manage.py migrate
   python manage.py collectstatic --noinput
   ```

7. **Create a superuser** (for admin access):
   ```bash
   python manage.py createsuperuser
   ```

8. **Start the development server**:
   ```bash
   python manage.py runserver
   ```

9. **Open your browser** to:
   - Main site: http://localhost:8000/
   - Admin panel: http://localhost:8000/admin/

**Success!** You now have a fully functional solar quote calculator with database storage.

---

### Option 3: Deploy to PythonAnywhere (Free Hosting) 🌐
**Best for:** Online deployment with free hosting

**Prerequisites:**
- Free PythonAnywhere account (https://www.pythonanywhere.com)

**Steps:**

1. **Sign up for free account** at PythonAnywhere

2. **Upload your code**:
   - Go to "Files" tab
   - Upload the entire project folder
   - Or use Git to clone your repository

3. **Create a virtual environment**:
   ```bash
   mkvirtualenv --python=/usr/bin/python3.10 myenv
   pip install -r requirements.txt
   ```

4. **Configure web app**:
   - Go to "Web" tab
   - Click "Add a new web app"
   - Choose "Manual configuration"
   - Select Python 3.10

5. **Set up WSGI file**:
   Click on the WSGI configuration file and edit:
   ```python
   import os
   import sys
   
   path = '/home/yourusername/Test-'
   if path not in sys.path:
       sys.path.append(path)
   
   os.environ['DJANGO_SETTINGS_MODULE'] = 'myproject.settings'
   
   from django.core.wsgi import get_wsgi_application
   application = get_wsgi_application()
   ```

6. **Configure static files**:
   In the Web tab, add:
   - URL: `/static/`
   - Directory: `/home/yourusername/Test-/staticfiles/`

7. **Run migrations**:
   ```bash
   cd ~/Test-
   python manage.py migrate
   python manage.py collectstatic
   ```

8. **Reload your web app** and visit your site at:
   `https://yourusername.pythonanywhere.com`

**Live!** Your solar calculator is now online and accessible worldwide.

---

## 📊 Quick Comparison

| Option | Setup Time | Persistence | Online Access | Best For |
|--------|-----------|-------------|---------------|----------|
| **Standalone HTML** | 0 seconds | No database | Local only | Quick demo/testing |
| **Django Local** | 5-10 minutes | Yes (database) | Local only | Development |
| **PythonAnywhere** | 15-20 minutes | Yes (database) | Yes (public) | Production hosting |

---

## 🎨 What You'll See

Once running, you'll have access to:

### User Interface:
- Clean, modern gradient design (purple/teal)
- Responsive form with 6 input fields:
  - ZIP Code
  - Monthly electricity bill
  - Roof size (sq ft)
  - Roof type (dropdown)
  - Sun exposure (dropdown)
  - Electricity rate

### Results Display:
- System size recommendation (kW)
- Number of solar panels needed
- Total system cost
- Federal tax credit (30%)
- Net cost after incentives
- Annual savings
- Payback period
- 25-year lifetime savings
- Environmental impact:
  - CO₂ offset (lbs/year)
  - Trees planted equivalent
  - Cars off road equivalent
  - Clean energy produced (MWh)

### Admin Panel (Django only):
- View all submitted quotes
- Filter by date, location, exposure
- Search by ZIP code
- Export data

---

## 🔧 Troubleshooting

### Standalone HTML Issues:
- **Form not submitting?** Make sure JavaScript is enabled in your browser
- **Styles not loading?** Try a different browser (Chrome, Firefox, Safari recommended)

### Django Issues:
- **"solar_quote not found"?** Make sure it's in INSTALLED_APPS
- **Static files not loading?** Run `python manage.py collectstatic`
- **Database errors?** Run `python manage.py migrate`
- **Port already in use?** Use `python manage.py runserver 8080`

### PythonAnywhere Issues:
- **500 Server Error?** Check error logs in the Web tab
- **Static files missing?** Verify static file configuration in Web tab
- **Can't access admin?** Make sure you created a superuser

---

## 📝 Next Steps

After getting it running:

1. **Test the calculator** with sample data:
   - ZIP: 90210
   - Bill: $250
   - Roof: 2000 sq ft
   - Type: Asphalt Shingles
   - Exposure: Excellent
   - Rate: $0.13/kWh

2. **Customize** (optional):
   - Modify colors in `solar_quote/static/css/style.css`
   - Adjust calculation parameters in `solar_quote/views.py`
   - Add your logo to the header

3. **Deploy to production**:
   - See `DEPLOYMENT_GUIDE.md` for Heroku, DigitalOcean, AWS, etc.
   - Configure custom domain
   - Set up SSL certificate

---

## 💡 Pro Tips

- **Quick testing?** → Use Option 1 (standalone HTML)
- **Want database?** → Use Option 2 (Django local)
- **Need it online?** → Use Option 3 (PythonAnywhere)
- **Need help?** → See `DJANGO_SETUP.md` or `DEPLOYMENT_GUIDE.md`

---

## 📞 Getting Help

If you get stuck:

1. Check the error message carefully
2. Review the relevant guide:
   - `DJANGO_SETUP.md` - Django integration
   - `DEPLOYMENT_GUIDE.md` - Online deployment
   - `solar_quote/README.md` - App details
3. Make sure all prerequisites are installed
4. Try the standalone HTML version first to verify it works

---

## ✅ Success Checklist

After following this guide, you should have:
- [ ] Calculator running in browser
- [ ] Form accepting inputs
- [ ] Results displaying correctly
- [ ] Mobile-responsive design working
- [ ] (Django only) Database storing quotes
- [ ] (Django only) Admin panel accessible

---

**Choose your option above and get started in minutes!** ☀️

**My recommendation:** Start with **Option 1** (standalone HTML) to see it work immediately, then move to **Option 2** (Django local) if you want to customize or deploy it online later.
