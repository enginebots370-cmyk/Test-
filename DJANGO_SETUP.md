# Solar Quote Engine - Django Integration Guide

A complete solar panel quote calculator built for Django. This application calculates solar system sizing, costs, savings, and environmental impact based on user inputs.

## 🌟 Features

- **Interactive Calculator**: Real-time solar quote calculations
- **Comprehensive Results**: System size, costs, savings, payback period
- **Environmental Impact**: CO2 offset, trees equivalent, clean energy production
- **Django Backend**: Full database integration for quote storage
- **REST API**: JSON API endpoint for calculations
- **Responsive Design**: Works on desktop, tablet, and mobile devices
- **Admin Interface**: Manage quotes through Django admin

## 📁 Project Structure

```
solar_quote/
├── __init__.py
├── admin.py              # Django admin configuration
├── apps.py               # App configuration
├── forms.py              # Django forms
├── models.py             # Database models
├── urls.py               # URL routing
├── views.py              # View logic and API endpoints
├── static/
│   ├── css/
│   │   └── style.css     # Stylesheet
│   └── js/
│       └── calculator.js  # Frontend JavaScript
└── templates/
    └── solar_quote/
        └── index.html     # Main template
```

## 🚀 Installation & Setup

### Step 1: Add to Django Project

1. Copy the `solar_quote` folder into your Django project directory

2. Add to `INSTALLED_APPS` in your `settings.py`:

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
```

### Step 2: Configure URLs

Add to your project's main `urls.py`:

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('solar_quote.urls')),  # Add this line
    # or use a prefix: path('solar/', include('solar_quote.urls')),
]
```

### Step 3: Configure Static Files

Ensure your `settings.py` has these settings:

```python
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'

# For development
STATICFILES_DIRS = []

# Optional: Configure media files if needed
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'
```

### Step 4: Run Migrations

```bash
python manage.py makemigrations solar_quote
python manage.py migrate
```

### Step 5: Create Superuser (for admin access)

```bash
python manage.py createsuperuser
```

### Step 6: Collect Static Files

```bash
python manage.py collectstatic
```

### Step 7: Run Development Server

```bash
python manage.py runserver
```

Visit: `http://localhost:8000/`

## 🔧 Configuration

### API Endpoint

The calculator uses a REST API endpoint at `/api/calculate/`:

- **Method**: POST
- **Content-Type**: application/json
- **CSRF Protection**: Required for Django

**Request Body**:
```json
{
    "zipCode": "90210",
    "monthlyBill": 250,
    "roofSize": 2000,
    "roofType": "asphalt",
    "sunExposure": "excellent",
    "electricityRate": 0.13
}
```

**Response**:
```json
{
    "success": true,
    "results": {
        "systemSize": 30.0,
        "panelCount": 90,
        "annualProduction": 36000,
        "coveragePercent": 100,
        "systemCost": 90000,
        "taxCredit": 27000,
        "netCost": 63000,
        "annualSavings": 4680,
        "paybackYears": 13.5,
        "lifetimeSavings": 54000,
        "co2Offset": 33120,
        "treesEquivalent": 690,
        "carsOffRoad": 3.68,
        "lifetimeEnergy": 900.0
    }
}
```

### Fallback Mode

The JavaScript includes client-side calculation as a fallback if the Django backend is not available. This ensures the calculator works even during development or if the API is temporarily unavailable.

## 🌐 Deployment

### For Production (Heroku, DigitalOcean, AWS, etc.)

1. **Update `settings.py` for production**:

```python
DEBUG = False
ALLOWED_HOSTS = ['yourdomain.com', 'www.yourdomain.com']

# Security settings
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_BROWSER_XSS_FILTER = True
```

2. **Use a production database** (PostgreSQL recommended):

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'your_db_name',
        'USER': 'your_db_user',
        'PASSWORD': 'your_db_password',
        'HOST': 'your_db_host',
        'PORT': '5432',
    }
}
```

3. **Use environment variables** for sensitive data:

```python
import os
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY')
DEBUG = os.environ.get('DEBUG', 'False') == 'True'
```

4. **Configure static files for production**:

```python
# Use WhiteNoise for serving static files
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # Add this
    # ... other middleware
]

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
```

Install WhiteNoise:
```bash
pip install whitenoise
```

5. **Create `requirements.txt`**:

```bash
pip freeze > requirements.txt
```

### Heroku Deployment

1. Install Heroku CLI and login:
```bash
heroku login
```

2. Create a new Heroku app:
```bash
heroku create your-solar-quote-app
```

3. Add PostgreSQL:
```bash
heroku addons:create heroku-postgresql:hobby-dev
```

4. Set environment variables:
```bash
heroku config:set DJANGO_SECRET_KEY='your-secret-key'
heroku config:set DEBUG=False
```

5. Create `Procfile`:
```
web: gunicorn your_project_name.wsgi
```

6. Deploy:
```bash
git push heroku main
heroku run python manage.py migrate
heroku run python manage.py createsuperuser
```

## 📊 Admin Interface

Access the Django admin at `/admin/` to:
- View all submitted quotes
- Filter by date, location, roof type, sun exposure
- Search by ZIP code or email
- Export data for analysis

## 🎨 Customization

### Modify Calculation Parameters

Edit `views.py` to adjust:
- `system_cost_per_watt`: Currently $3.00/watt
- `tax_credit`: Currently 30% federal credit
- Solar production estimates: Currently 1,200 kWh/kW/year
- CO2 offset rate: 0.92 lbs/kWh

### Styling

Customize colors and design in `static/css/style.css`:
- Primary gradient: `#667eea` to `#764ba2`
- Savings highlight: `#11998e` to `#38ef7d`

### Add Email Notifications

To send quotes via email, add to `views.py`:

```python
from django.core.mail import send_mail

# In calculate_quote view, after saving:
send_mail(
    'Your Solar Quote',
    f'Your estimated savings: ${annual_savings}',
    'from@example.com',
    [request.user.email],
    fail_silently=False,
)
```

## 🧪 Testing

Run tests:
```bash
python manage.py test solar_quote
```

## 📱 Mobile Responsiveness

The application automatically adapts to:
- Desktop (1200px+)
- Tablet (768px - 1200px)
- Mobile (< 768px)

## 🔒 Security

- CSRF protection enabled
- Input validation on client and server
- SQL injection protection via Django ORM
- XSS protection via Django templates

## 📝 License

This project is open source and available for modification.

## 🤝 Support

For issues or questions:
1. Check the Django documentation
2. Review the code comments
3. Test in development mode first
4. Check browser console for JavaScript errors

## 🚀 Quick Start Checklist

- [ ] Copy `solar_quote` folder to Django project
- [ ] Add to `INSTALLED_APPS`
- [ ] Configure URLs
- [ ] Run migrations
- [ ] Collect static files
- [ ] Test locally
- [ ] Create superuser
- [ ] Configure production settings
- [ ] Deploy to hosting service
- [ ] Set up domain and SSL

## 📈 Future Enhancements

Consider adding:
- Email quote delivery
- PDF quote generation
- Integration with solar panel suppliers
- Financing calculator
- Multiple location comparison
- Seasonal production estimates
- Battery storage calculations
- User accounts and saved quotes

---

**Built with Django 🌐 | Powered by Solar Energy ☀️**
