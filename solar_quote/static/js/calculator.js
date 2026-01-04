// Solar Quote Engine JavaScript

document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('solarForm');
    
    if (form) {
        form.addEventListener('submit', function(e) {
            e.preventDefault();
            calculateQuote();
        });
    }
});

function calculateQuote() {
    // Clear previous errors
    document.querySelectorAll('.error').forEach(el => el.classList.remove('show'));
    
    // Get form values
    const zipCode = document.getElementById('zipCode').value;
    const monthlyBill = parseFloat(document.getElementById('monthlyBill').value);
    const roofSize = parseFloat(document.getElementById('roofSize').value);
    const roofType = document.getElementById('roofType').value;
    const sunExposure = document.getElementById('sunExposure').value;
    const electricityRate = parseFloat(document.getElementById('electricityRate').value);
    
    // Validate inputs
    let isValid = true;
    
    if (monthlyBill <= 0 || isNaN(monthlyBill)) {
        const error = document.getElementById('billError');
        if (error) error.classList.add('show');
        isValid = false;
    }
    
    if (roofSize <= 0 || isNaN(roofSize)) {
        const error = document.getElementById('roofError');
        if (error) error.classList.add('show');
        isValid = false;
    }
    
    if (!isValid) return;
    
    // Show loading
    const loading = document.querySelector('.loading');
    if (loading) loading.classList.add('show');
    
    // Prepare data
    const data = {
        zipCode: zipCode,
        monthlyBill: monthlyBill,
        roofSize: roofSize,
        roofType: roofType,
        sunExposure: sunExposure,
        electricityRate: electricityRate
    };
    
    // Get CSRF token for Django
    const csrftoken = getCookie('csrftoken');
    
    // Send to server (Django backend)
    fetch('/api/calculate/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken
        },
        body: JSON.stringify(data)
    })
    .then(response => response.json())
    .then(data => {
        if (loading) loading.classList.remove('show');
        
        if (data.success) {
            displayResults(data.results);
        } else {
            alert('Error calculating quote: ' + (data.error || 'Unknown error'));
        }
    })
    .catch(error => {
        if (loading) loading.classList.remove('show');
        console.error('Error:', error);
        // Fallback to client-side calculation if server is not available
        calculateClientSide(data);
    });
}

function calculateClientSide(data) {
    // Client-side calculation as fallback
    const annualConsumption = (data.monthlyBill / data.electricityRate) * 12;
    
    const sunMultipliers = {
        'excellent': 1.0,
        'good': 0.85,
        'moderate': 0.7,
        'limited': 0.5
    };
    
    const sunMultiplier = sunMultipliers[data.sunExposure];
    const maxSystemSize = (data.roofSize / 100) * 1.5 * sunMultiplier;
    const estimatedProduction = maxSystemSize * 1200 * sunMultiplier;
    const coveragePercent = Math.min((estimatedProduction / annualConsumption) * 100, 100);
    const systemCost = maxSystemSize * 1000 * 3.0;
    const taxCredit = systemCost * 0.30;
    const netCost = systemCost - taxCredit;
    const annualSavings = (estimatedProduction * data.electricityRate) * (coveragePercent / 100);
    const paybackYears = netCost / annualSavings;
    const lifetimeSavings = (annualSavings * 25) - netCost;
    const co2Offset = estimatedProduction * 0.92;
    const treesEquivalent = Math.round(co2Offset / 48);
    const carsOffRoad = (co2Offset / 9000).toFixed(2);
    
    const results = {
        systemSize: maxSystemSize.toFixed(2),
        panelCount: Math.round(maxSystemSize * 3),
        annualProduction: estimatedProduction.toFixed(0),
        coveragePercent: coveragePercent.toFixed(0),
        systemCost: systemCost.toFixed(0),
        taxCredit: taxCredit.toFixed(0),
        netCost: netCost.toFixed(0),
        annualSavings: annualSavings.toFixed(0),
        paybackYears: paybackYears.toFixed(1),
        lifetimeSavings: lifetimeSavings.toFixed(0),
        co2Offset: co2Offset.toFixed(0),
        treesEquivalent: treesEquivalent,
        carsOffRoad: carsOffRoad,
        lifetimeEnergy: ((estimatedProduction * 25) / 1000).toFixed(1)
    };
    
    displayResults(results);
}

function displayResults(results) {
    const resultsHTML = `
        <div class="result-item">
            <h3>Recommended System Size</h3>
            <div class="result-value">${results.systemSize} kW</div>
            <div class="result-description">${results.panelCount} solar panels (approx.)</div>
        </div>
        
        <div class="result-item">
            <h3>Estimated Annual Production</h3>
            <div class="result-value">${formatNumber(results.annualProduction)} kWh</div>
            <div class="result-description">Covers ${results.coveragePercent}% of your electricity needs</div>
        </div>
        
        <div class="result-item">
            <h3>System Cost</h3>
            <div class="result-value">$${formatNumber(results.systemCost)}</div>
            <div class="result-description">Before incentives</div>
        </div>
        
        <div class="result-item">
            <h3>Federal Tax Credit (30%)</h3>
            <div class="result-value">-$${formatNumber(results.taxCredit)}</div>
            <div class="result-description">Net cost: $${formatNumber(results.netCost)}</div>
        </div>
        
        <div class="result-item savings-highlight">
            <h3>Annual Savings</h3>
            <div class="result-value">$${formatNumber(results.annualSavings)}</div>
            <div class="result-description">Payback period: ${results.paybackYears} years</div>
        </div>
        
        <div class="result-item savings-highlight">
            <h3>25-Year Lifetime Savings</h3>
            <div class="result-value">$${formatNumber(results.lifetimeSavings)}</div>
            <div class="result-description">Total savings after system pays for itself</div>
        </div>
        
        <div class="result-item">
            <h3>Environmental Impact</h3>
            <div class="environmental-impact">
                <div class="impact-item">
                    <div class="impact-value">${formatNumber(results.co2Offset)}</div>
                    <div class="impact-label">lbs CO₂ offset/year</div>
                </div>
                <div class="impact-item">
                    <div class="impact-value">${results.treesEquivalent}</div>
                    <div class="impact-label">trees planted equivalent</div>
                </div>
                <div class="impact-item">
                    <div class="impact-value">${results.carsOffRoad}</div>
                    <div class="impact-label">cars off road/year</div>
                </div>
                <div class="impact-item">
                    <div class="impact-value">${results.lifetimeEnergy}</div>
                    <div class="impact-label">MWh clean energy (25yr)</div>
                </div>
            </div>
        </div>
    `;
    
    document.getElementById('resultsContent').innerHTML = resultsHTML;
    document.getElementById('resultsCard').classList.add('show');
    
    // Smooth scroll to results
    document.getElementById('resultsCard').scrollIntoView({ behavior: 'smooth', block: 'nearest' });
}

function formatNumber(num) {
    return parseFloat(num).toFixed(0).replace(/\B(?=(\d{3})+(?!\d))/g, ",");
}

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
