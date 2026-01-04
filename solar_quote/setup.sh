#!/bin/bash
# Quick Setup Script for Solar Quote Engine Django App

echo "🌞 Solar Quote Engine - Quick Setup"
echo "===================================="
echo ""

# Check if Django is installed
if ! python -c "import django" &> /dev/null; then
    echo "⚠️  Django is not installed. Installing..."
    pip install -r requirements.txt
fi

echo "✓ Django is installed"
echo ""

# Check if manage.py exists in parent directory
if [ ! -f "../manage.py" ]; then
    echo "⚠️  Warning: manage.py not found in parent directory"
    echo "   Make sure you've placed solar_quote/ in your Django project root"
    echo ""
    read -p "Continue anyway? (y/n) " -n 1 -r
    echo ""
    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
        exit 1
    fi
fi

# Find the Django project directory
PROJECT_DIR="../"
if [ -f "../manage.py" ]; then
    PROJECT_DIR="../"
fi

echo "📝 Creating migrations..."
cd $PROJECT_DIR
python manage.py makemigrations solar_quote

echo ""
echo "🔄 Running migrations..."
python manage.py migrate

echo ""
echo "📦 Collecting static files..."
python manage.py collectstatic --noinput

echo ""
echo "✨ Setup complete!"
echo ""
echo "Next steps:"
echo "1. Make sure 'solar_quote' is in INSTALLED_APPS (see SETTINGS_EXAMPLE.py)"
echo "2. Add URL configuration (see URLS_EXAMPLE.py)"
echo "3. Create a superuser: python manage.py createsuperuser"
echo "4. Run the server: python manage.py runserver"
echo ""
echo "📖 Full documentation: DJANGO_SETUP.md"
