# Solar Quote Engine - Django App

A production-ready Django application for calculating solar panel quotes, costs, and savings.

## 📦 What's Included

```
solar_quote/
├── __init__.py              # Package initialization
├── admin.py                 # Django admin configuration
├── apps.py                  # App configuration
├── forms.py                 # Form definitions
├── models.py                # Database models
├── tests.py                 # Unit tests
├── urls.py                  # URL routing
├── views.py                 # Views and API endpoints
├── setup.sh                 # Quick setup script
├── SETTINGS_EXAMPLE.py      # Django settings examples
├── URLS_EXAMPLE.py          # URL configuration examples
├── static/
│   ├── css/
│   │   └── style.css        # Responsive stylesheet
│   └── js/
│       └── calculator.js    # Frontend calculator logic
└── templates/
    └── solar_quote/
        └── index.html       # Main template
```

## 🚀 Quick Start

### 1. Installation

Copy this `solar_quote` folder to your Django project directory:

```bash
your_django_project/
├── manage.py
├── your_project/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── solar_quote/           ← Copy this folder here
```

### 2. Add to Django

Edit your `settings.py`:

```python
INSTALLED_APPS = [
    # ... existing apps
    'solar_quote',  # Add this
]
```

### 3. Configure URLs

Edit your project's `urls.py`:

```python
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('solar_quote.urls')),  # Add this
]
```

### 4. Run Setup

```bash
# Option A: Use the setup script
cd solar_quote
./setup.sh

# Option B: Manual setup
cd ..  # Go to project root
python manage.py makemigrations solar_quote
python manage.py migrate
python manage.py collectstatic
```

### 5. Create Superuser

```bash
python manage.py createsuperuser
```

### 6. Run Server

```bash
python manage.py runserver
```

Visit: http://localhost:8000/

## 📊 Database Models

### SolarQuote Model

Stores solar quote requests with the following fields:

- **User Input**:
  - `zip_code` - Location ZIP code
  - `monthly_bill` - Average monthly electricity bill
  - `roof_size` - Roof size in square feet
  - `roof_type` - Type of roof (asphalt, metal, tile, flat)
  - `sun_exposure` - Sun exposure level (excellent, good, moderate, limited)
  - `electricity_rate` - Cost per kWh
  - `email` - Optional contact email

- **Calculated Results**:
  - `system_size_kw` - Recommended system size
  - `annual_production_kwh` - Annual energy production
  - `system_cost` - Total system cost
  - `annual_savings` - Estimated annual savings

- **Metadata**:
  - `created_at` - Timestamp of quote request
  - `updated_at` - Last update timestamp

## 🔌 API Endpoints

### POST /api/calculate/

Calculate solar quote based on user input.

**Request**:
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

## 🎨 Customization

### Calculation Parameters

Edit `views.py` to modify:

```python
# Cost per watt (default: $3.00)
system_cost_per_watt = 3.0

# Federal tax credit (default: 30%)
tax_credit = system_cost * 0.30

# Annual production per kW (default: 1,200 kWh)
estimated_production = max_system_size * 1200 * sun_multiplier

# CO2 offset rate (default: 0.92 lbs per kWh)
co2_offset = estimated_production * 0.92
```

### Styling

Edit `static/css/style.css` to change:
- Colors and gradients
- Layout and spacing
- Font sizes and families
- Responsive breakpoints

### Sun Exposure Multipliers

Edit in `views.py`:

```python
sun_multipliers = {
    'excellent': 1.0,   # Full sun all day
    'good': 0.85,       # 6-8 hours
    'moderate': 0.7,    # 4-6 hours
    'limited': 0.5      # Less than 4 hours
}
```

## 🧪 Testing

Run the included unit tests:

```bash
python manage.py test solar_quote
```

Tests cover:
- Model creation and validation
- View responses
- API endpoints
- Calculation logic
- Database operations

## 🔐 Admin Interface

Access at `/admin/` to:
- View all submitted quotes
- Filter by date, location, exposure
- Search by ZIP code or email
- Export data for analysis

Fields displayed:
- ZIP code
- Monthly bill
- System size (kW)
- Annual savings
- Creation date

## 📱 Features

### Client-Side (JavaScript)
- Real-time form validation
- CSRF token handling
- Fallback calculation if API unavailable
- Smooth scrolling to results
- Number formatting with commas

### Server-Side (Django)
- Database persistence
- RESTful API
- Input validation
- Error handling
- Admin interface

### Design
- Responsive grid layout
- Mobile-first approach
- Gradient color scheme
- Modern card-based UI
- Clear visual hierarchy

## 🌐 Deployment

See the main project's `DEPLOYMENT_GUIDE.md` for detailed instructions on deploying to:
- Heroku
- DigitalOcean
- PythonAnywhere
- Railway
- AWS

## 📋 Requirements

Minimum requirements:
- Django 4.2+
- Python 3.8+

For production, also install:
- `gunicorn` - WSGI server
- `psycopg2-binary` - PostgreSQL adapter
- `whitenoise` - Static file serving
- `dj-database-url` - Database URL parsing

See `requirements.txt` in project root.

## 🔧 Troubleshooting

### Static Files Not Loading

```bash
python manage.py collectstatic --clear
```

Make sure `STATIC_ROOT` is set in settings.

### Template Not Found

Verify folder structure:
```
solar_quote/templates/solar_quote/index.html
```

### Database Errors

```bash
python manage.py makemigrations
python manage.py migrate
```

### ImportError

Make sure `solar_quote` is in `INSTALLED_APPS` and you've restarted the server.

## 📞 Support

- See `DJANGO_SETUP.md` for detailed setup instructions
- See `DEPLOYMENT_GUIDE.md` for deployment help
- Check Django documentation: https://docs.djangoproject.com/
- Review the code comments for inline documentation

## 📄 License

Open source - free to use and modify for your projects.

---

**Built with Django | Powered by Solar Energy ☀️**
