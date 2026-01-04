# Example Django settings.py additions
# Add these to your existing Django settings.py file

# Add to INSTALLED_APPS
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'solar_quote',  # <-- Add this
]

# Static files configuration
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'

# Media files (optional)
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# For production with WhiteNoise
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # <-- Add this for production
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Production settings (use environment variables)
# import os
# SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'dev-secret-key')
# DEBUG = os.environ.get('DEBUG', 'False') == 'True'
# ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', 'localhost').split(',')
