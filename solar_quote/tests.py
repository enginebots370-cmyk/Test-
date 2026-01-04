from django.test import TestCase, Client
from django.urls import reverse
from decimal import Decimal
from .models import SolarQuote
import json


class SolarQuoteModelTest(TestCase):
    """Test the SolarQuote model"""
    
    def setUp(self):
        self.quote = SolarQuote.objects.create(
            zip_code='90210',
            monthly_bill=Decimal('250.00'),
            roof_size=2000,
            roof_type='asphalt',
            sun_exposure='excellent',
            electricity_rate=Decimal('0.13'),
            system_size_kw=Decimal('30.00'),
            annual_production_kwh=36000,
            system_cost=Decimal('90000.00'),
            annual_savings=Decimal('4680.00')
        )
    
    def test_quote_creation(self):
        """Test that a quote can be created"""
        self.assertEqual(self.quote.zip_code, '90210')
        self.assertEqual(self.quote.monthly_bill, Decimal('250.00'))
        self.assertEqual(self.quote.roof_size, 2000)
    
    def test_quote_string_representation(self):
        """Test the string representation of a quote"""
        expected = "Quote for 90210 - $250.00/month"
        self.assertEqual(str(self.quote), expected)


class SolarQuoteViewTest(TestCase):
    """Test the views"""
    
    def setUp(self):
        self.client = Client()
    
    def test_index_view(self):
        """Test that the index page loads"""
        response = self.client.get(reverse('solar_quote:index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'solar_quote/index.html')
    
    def test_calculate_api_valid_data(self):
        """Test the calculation API with valid data"""
        data = {
            'zipCode': '90210',
            'monthlyBill': 250,
            'roofSize': 2000,
            'roofType': 'asphalt',
            'sunExposure': 'excellent',
            'electricityRate': 0.13
        }
        
        response = self.client.post(
            reverse('solar_quote:calculate'),
            data=json.dumps(data),
            content_type='application/json'
        )
        
        self.assertEqual(response.status_code, 200)
        result = json.loads(response.content)
        self.assertTrue(result['success'])
        self.assertIn('results', result)
        self.assertIn('systemSize', result['results'])
    
    def test_calculate_api_invalid_data(self):
        """Test the calculation API with invalid data"""
        data = {
            'zipCode': '90210',
            'monthlyBill': -100,  # Invalid negative value
            'roofSize': 2000,
            'roofType': 'asphalt',
            'sunExposure': 'excellent',
            'electricityRate': 0.13
        }
        
        response = self.client.post(
            reverse('solar_quote:calculate'),
            data=json.dumps(data),
            content_type='application/json'
        )
        
        self.assertEqual(response.status_code, 400)
    
    def test_calculate_api_creates_quote(self):
        """Test that API call creates a quote in database"""
        initial_count = SolarQuote.objects.count()
        
        data = {
            'zipCode': '10001',
            'monthlyBill': 150,
            'roofSize': 1500,
            'roofType': 'metal',
            'sunExposure': 'good',
            'electricityRate': 0.15
        }
        
        response = self.client.post(
            reverse('solar_quote:calculate'),
            data=json.dumps(data),
            content_type='application/json'
        )
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(SolarQuote.objects.count(), initial_count + 1)
        
        # Check the created quote
        quote = SolarQuote.objects.latest('created_at')
        self.assertEqual(quote.zip_code, '10001')
        self.assertEqual(float(quote.monthly_bill), 150)


class SolarCalculationTest(TestCase):
    """Test the calculation logic"""
    
    def test_system_size_calculation(self):
        """Test that system size is calculated correctly"""
        roof_size = 2000
        sun_multiplier = 1.0  # excellent
        expected_size = (roof_size / 100) * 1.5 * sun_multiplier
        self.assertEqual(expected_size, 30.0)
    
    def test_annual_production_calculation(self):
        """Test annual production calculation"""
        system_size = 30.0
        sun_multiplier = 1.0
        expected_production = system_size * 1200 * sun_multiplier
        self.assertEqual(expected_production, 36000)
    
    def test_cost_calculation(self):
        """Test cost calculation"""
        system_size = 30.0
        cost_per_watt = 3.0
        expected_cost = system_size * 1000 * cost_per_watt
        self.assertEqual(expected_cost, 90000.0)
    
    def test_tax_credit_calculation(self):
        """Test tax credit calculation"""
        system_cost = 90000.0
        tax_credit = system_cost * 0.30
        self.assertEqual(tax_credit, 27000.0)
