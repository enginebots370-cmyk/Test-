from django.db import models
from django.core.validators import MinValueValidator


class SolarQuote(models.Model):
    """Model to store solar quote requests"""
    
    ROOF_TYPES = [
        ('asphalt', 'Asphalt Shingles'),
        ('metal', 'Metal'),
        ('tile', 'Tile'),
        ('flat', 'Flat'),
    ]
    
    SUN_EXPOSURE = [
        ('excellent', 'Excellent (Full sun all day)'),
        ('good', 'Good (6-8 hours)'),
        ('moderate', 'Moderate (4-6 hours)'),
        ('limited', 'Limited (Less than 4 hours)'),
    ]
    
    # User Information
    zip_code = models.CharField(max_length=10, verbose_name="ZIP Code")
    monthly_bill = models.DecimalField(
        max_digits=10, 
        decimal_places=2, 
        validators=[MinValueValidator(0)],
        verbose_name="Monthly Electricity Bill"
    )
    roof_size = models.IntegerField(
        validators=[MinValueValidator(0)],
        verbose_name="Roof Size (sq ft)"
    )
    roof_type = models.CharField(max_length=20, choices=ROOF_TYPES, default='asphalt')
    sun_exposure = models.CharField(max_length=20, choices=SUN_EXPOSURE, default='excellent')
    electricity_rate = models.DecimalField(
        max_digits=5, 
        decimal_places=2, 
        validators=[MinValueValidator(0)],
        default=0.13,
        verbose_name="Electricity Rate ($/kWh)"
    )
    
    # Calculated Results (stored for reference)
    system_size_kw = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    annual_production_kwh = models.IntegerField(null=True, blank=True)
    system_cost = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    annual_savings = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    
    # Metadata
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    email = models.EmailField(blank=True, null=True, verbose_name="Contact Email")
    
    class Meta:
        ordering = ['-created_at']
        verbose_name = "Solar Quote"
        verbose_name_plural = "Solar Quotes"
    
    def __str__(self):
        return f"Quote for {self.zip_code} - ${self.monthly_bill}/month"
