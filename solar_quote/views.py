from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from .forms import SolarQuoteForm
from .models import SolarQuote
import json


def index(request):
    """Main view for solar quote calculator"""
    form = SolarQuoteForm()
    return render(request, 'solar_quote/index.html', {'form': form})


@require_http_methods(["POST"])
def calculate_quote(request):
    """API endpoint to calculate solar quote"""
    try:
        data = json.loads(request.body)
        
        # Extract form values
        monthly_bill = float(data.get('monthlyBill', 0))
        roof_size = float(data.get('roofSize', 0))
        sun_exposure = data.get('sunExposure', 'excellent')
        electricity_rate = float(data.get('electricityRate', 0.13))
        zip_code = data.get('zipCode', '')
        roof_type = data.get('roofType', 'asphalt')
        
        # Validate inputs
        if monthly_bill <= 0 or roof_size <= 0:
            return JsonResponse({'error': 'Invalid input values'}, status=400)
        
        # Calculate solar system specifications
        annual_consumption = (monthly_bill / electricity_rate) * 12  # kWh per year
        
        # Sun exposure multiplier
        sun_multipliers = {
            'excellent': 1.0,
            'good': 0.85,
            'moderate': 0.7,
            'limited': 0.5
        }
        sun_multiplier = sun_multipliers.get(sun_exposure, 1.0)
        
        # Calculate system size (typical panel produces 1.5 kW per 100 sq ft)
        max_system_size = (roof_size / 100) * 1.5 * sun_multiplier
        
        # Typical solar panel produces ~1,200 kWh per kW per year
        estimated_production = max_system_size * 1200 * sun_multiplier
        
        # Calculate coverage percentage
        coverage_percent = min((estimated_production / annual_consumption) * 100, 100)
        
        # Cost calculations ($3 per watt is typical)
        system_cost_per_watt = 3.0
        system_cost = max_system_size * 1000 * system_cost_per_watt
        
        # Federal tax credit (30%)
        tax_credit = system_cost * 0.30
        net_cost = system_cost - tax_credit
        
        # Annual savings
        annual_savings = (estimated_production * electricity_rate) * (coverage_percent / 100)
        
        # Payback period
        payback_years = net_cost / annual_savings if annual_savings > 0 else 0
        
        # 25-year savings
        lifetime_savings = (annual_savings * 25) - net_cost
        
        # Environmental impact
        co2_offset = estimated_production * 0.92  # lbs per year
        trees_equivalent = round(co2_offset / 48)
        cars_off_road = round(co2_offset / 9000, 2)
        lifetime_energy = round((estimated_production * 25) / 1000, 1)
        
        # Save to database (optional)
        quote = SolarQuote.objects.create(
            zip_code=zip_code,
            monthly_bill=monthly_bill,
            roof_size=roof_size,
            roof_type=roof_type,
            sun_exposure=sun_exposure,
            electricity_rate=electricity_rate,
            system_size_kw=max_system_size,
            annual_production_kwh=int(estimated_production),
            system_cost=system_cost,
            annual_savings=annual_savings
        )
        
        # Return calculated results
        return JsonResponse({
            'success': True,
            'results': {
                'systemSize': round(max_system_size, 2),
                'panelCount': round(max_system_size * 3),
                'annualProduction': round(estimated_production),
                'coveragePercent': round(coverage_percent),
                'systemCost': round(system_cost),
                'taxCredit': round(tax_credit),
                'netCost': round(net_cost),
                'annualSavings': round(annual_savings),
                'paybackYears': round(payback_years, 1),
                'lifetimeSavings': round(lifetime_savings),
                'co2Offset': round(co2_offset),
                'treesEquivalent': trees_equivalent,
                'carsOffRoad': cars_off_road,
                'lifetimeEnergy': lifetime_energy
            }
        })
        
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)
