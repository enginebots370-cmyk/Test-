from django.contrib import admin
from .models import SolarQuote


@admin.register(SolarQuote)
class SolarQuoteAdmin(admin.ModelAdmin):
    list_display = ['zip_code', 'monthly_bill', 'system_size_kw', 'annual_savings', 'created_at']
    list_filter = ['sun_exposure', 'roof_type', 'created_at']
    search_fields = ['zip_code', 'email']
    readonly_fields = ['created_at', 'updated_at']
    
    fieldsets = (
        ('User Information', {
            'fields': ('zip_code', 'email', 'monthly_bill', 'roof_size', 'roof_type', 'sun_exposure', 'electricity_rate')
        }),
        ('Calculated Results', {
            'fields': ('system_size_kw', 'annual_production_kwh', 'system_cost', 'annual_savings')
        }),
        ('Metadata', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
