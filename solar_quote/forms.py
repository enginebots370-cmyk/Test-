from django import forms
from .models import SolarQuote


class SolarQuoteForm(forms.ModelForm):
    """Form for solar quote calculator"""
    
    class Meta:
        model = SolarQuote
        fields = ['zip_code', 'monthly_bill', 'roof_size', 'roof_type', 'sun_exposure', 'electricity_rate', 'email']
        widgets = {
            'zip_code': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your ZIP code',
            }),
            'monthly_bill': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': '150',
                'min': '0',
                'step': '1',
            }),
            'roof_size': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': '1500',
                'min': '0',
                'step': '50',
            }),
            'roof_type': forms.Select(attrs={'class': 'form-control'}),
            'sun_exposure': forms.Select(attrs={'class': 'form-control'}),
            'electricity_rate': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': '0.13',
                'min': '0',
                'step': '0.01',
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'your@email.com (optional)',
            }),
        }
